"""
Apple Hyperspectral Imaging & Defect Analysis Viewer
(Trinh xem du lieu sieu pho va phan tich khuyet tat tren qua tao)

Moi truong:
    conda activate hsi
    python python/view_apple_data.py

Ho tro:
1. CHE DO PCA (7 PCs):
   - 7 thanh phan chinh tu mo hinh PCA (vis_nir & nir) cho cac dang benh: Ri da (Rusty), Nam thoi (Fungus), Sau can (Insect Bite)
   - Do diem so PCA Scores (PC1 - PC7) tai tung pixel (bieu do cot Bar Chart)
   - Anh quet quay tron mo phang (colorimage.bmp) va ban do phan loai SVM 7 lop (SVM_7_topbottom_1603.bmp)

2. CHE DO BANG DO PHO HSI (600 BANDS):
   - 600 kenh buoc song quang pho tu 362 nm den 1018 nm
   - Do duong cong pho phan xa thuc te (Spectral Reflectance Profile) tai pixel duoc click
   - So sanh duong pho giua vung vo lanh (Normal area) va vung bi giap/thoi (Bruise area)
"""

import os
import sys
import argparse
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons, Button
from PIL import Image
import h5py

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))

def resolve_path(rel_path):
    # Tim theo PROJECT_ROOT truoc, neu khong thay thi tim theo SCRIPT_DIR
    p1 = os.path.join(PROJECT_ROOT, rel_path)
    if os.path.exists(p1):
        return p1
    p2 = os.path.join(SCRIPT_DIR, rel_path)
    if os.path.exists(p2):
        return p2
    return p1

def load_all_data():
    data_dict = {}
    
    # 1. PCA Data
    p_vis = resolve_path("data/pca_data/vis_nir.mat")
    if os.path.exists(p_vis):
        data_dict['vis_nir'] = sio.loadmat(p_vis)
        
    p_nir = resolve_path("data/pca_data/nir.mat")
    if os.path.exists(p_nir):
        data_dict['nir'] = sio.loadmat(p_nir)
        
    # 2. Scan images
    p_color = resolve_path("data/scan_images/colorimage.bmp")
    if os.path.exists(p_color):
        data_dict['color_image'] = np.array(Image.open(p_color))
        
    p_svm = resolve_path("data/scan_images/SVM_7_topbottom_1603.bmp")
    if os.path.exists(p_svm):
        data_dict['svm_pred'] = np.array(Image.open(p_svm))
        
    # 3. HSI Cube Data (uu tien file full, fallback sang file sample)
    p_hsi = resolve_path("data/hsi_cube/HSIdata20_r1.mat")
    if not os.path.exists(p_hsi):
        p_hsi = resolve_path("data/hsi_cube/HSIdata20_sample.mat")
        
    if os.path.exists(p_hsi):
        try:
            hf = h5py.File(p_hsi, 'r')
            data_dict['hsi_file'] = hf
            data_dict['hsi_data'] = hf['hsidata/data']
            data_dict['hsi_mask_obj'] = np.array(hf['hsidata/mask_object'])
            data_dict['hsi_mask_norm'] = np.array(hf['hsidata/mask_normal'])
            data_dict['hsi_mask_bruise'] = np.array(hf['hsidata/mask_bruise'])
            
            p_fac = resolve_path("data/calibration/factor_aca1920_155um_03_2020.mat")
            if not os.path.exists(p_fac):
                p_fac = resolve_path("data/calibration/factor.mat")
            if os.path.exists(p_fac):
                fac_mat = sio.loadmat(p_fac)
                p_coef = fac_mat['p'][0]
            else:
                p_coef = [1.09611204, 360.69232077]
                
            bands_arr = np.arange(1, 601)
            data_dict['wavelengths'] = p_coef[0] * bands_arr + p_coef[1]
            
            # Tinh duong pho trung binh Normal va Bruise
            ny, nx = np.where(data_dict['hsi_mask_norm'] > 0)
            if len(ny) > 0:
                sub_norm = data_dict['hsi_data'][:, ny.min():ny.max()+1, nx.min():nx.max()+1]
                m_sub = data_dict['hsi_mask_norm'][ny.min():ny.max()+1, nx.min():nx.max()+1] > 0
                data_dict['mean_norm_spec'] = np.mean(sub_norm[:, m_sub], axis=1)
            else:
                data_dict['mean_norm_spec'] = None
                
            by, bx = np.where(data_dict['hsi_mask_bruise'] > 0)
            if len(by) > 0:
                sub_bruise = data_dict['hsi_data'][:, by.min():by.max()+1, bx.min():bx.max()+1]
                m_sub_b = data_dict['hsi_mask_bruise'][by.min():by.max()+1, bx.min():bx.max()+1] > 0
                data_dict['mean_bruise_spec'] = np.mean(sub_bruise[:, m_sub_b], axis=1)
            else:
                data_dict['mean_bruise_spec'] = None
                
            print(f"[+] Loaded HSI Cube from: {os.path.basename(p_hsi)}")
        except Exception as e:
            print(f"[!] Warning reading HSI Cube: {e}")
            
    return data_dict

def run_viewer(data_dict):
    has_hsi = 'hsi_data' in data_dict
    current_cmap = 'gray'
    
    fig = plt.figure(figsize=(15.5, 9.0))
    try:
        fig.canvas.manager.set_window_title("Apple HSI & PCA Data Viewer - conda: hsi")
    except Exception:
        pass
        
    plt.subplots_adjust(left=0.07, bottom=0.20, right=0.93, top=0.91, wspace=0.28, hspace=0.32)
    
    ax_img1 = plt.subplot2grid((2, 4), (0, 0), colspan=1, rowspan=1)
    ax_img2 = plt.subplot2grid((2, 4), (0, 1), colspan=1, rowspan=1)
    ax_img3 = plt.subplot2grid((2, 4), (0, 2), colspan=1, rowspan=1)
    ax_plot = plt.subplot2grid((2, 4), (0, 3), colspan=1, rowspan=1)
    ax_bottom = plt.subplot2grid((2, 4), (1, 0), colspan=4, rowspan=1)
    
    pca_defects = ['rusty', 'fungus_infection', 'insect_bite']
    pca_titles = [
        "Tao bi ri da (Rusty)",
        "Tao bi nam/thoi (Fungus)",
        "Tao bi sau can (Insect Bite)"
    ]
    pc_labels = [f"PC{i}" for i in range(1, 8)]
    pc_colors = ['#3498db', '#2ecc71', '#e74c3c', '#9b59b6', '#f39c12', '#1abc9c', '#d35400']
    
    ax_slider = plt.axes([0.15, 0.09, 0.48, 0.03], facecolor='#ecf0f1')
    slider = Slider(ax_slider, 'Thanh phan PC: ', 1, 7, valinit=1, valstep=1, color='#2980b9')
    
    ax_radio_mode = plt.axes([0.68, 0.03, 0.16, 0.12], facecolor='#fbfbfb')
    modes_list = []
    if 'vis_nir' in data_dict: modes_list.append("PCA: 7 PCs (vis_nir)")
    if 'nir' in data_dict: modes_list.append("PCA: 7 PCs (nir)")
    if has_hsi: modes_list.append("HSI: Bang do pho (600 Bands)")
    radio_mode = RadioButtons(ax_radio_mode, modes_list, active=0)
    
    ax_radio_cmap = plt.axes([0.86, 0.03, 0.08, 0.12], facecolor='#fbfbfb')
    radio_cmap = RadioButtons(ax_radio_cmap, ['gray', 'jet', 'viridis', 'plasma'], active=0)
    
    ax_btn = plt.axes([0.15, 0.035, 0.20, 0.035])
    btn_toggle = Button(ax_btn, 'Doi anh duoi: RGB / SVM', color='#eaeded', hovercolor='#d5dbdb')
    bottom_state = {'view': 'color'}
    last_click = {'x': 250, 'y': 250, 'defect': 'rusty'}

    def render_pca():
        mat_key = 'vis_nir' if 'vis_nir' in radio_mode.value_selected else 'nir'
        mat = data_dict[mat_key]
        pc_idx = int(slider.val) - 1
        
        for ax, def_k, tit in zip([ax_img1, ax_img2, ax_img3], pca_defects, pca_titles):
            ax.clear()
            ax.imshow(mat[def_k][:, :, pc_idx], cmap=current_cmap)
            ax.set_title(f"{tit}\n[PC {pc_idx + 1}]", fontsize=10, fontweight='bold')
            ax.axis('off')
            
        ax_plot.clear()
        def_k = last_click['defect']
        cx, cy = last_click['x'], last_click['y']
        arr_3d = mat[def_k]
        h, w, nb = arr_3d.shape
        scores = arr_3d[cy, cx, :] if (0 <= cy < h and 0 <= cx < w) else np.zeros(7)
            
        bars = ax_plot.bar(pc_labels, scores, color=pc_colors, width=0.6, edgecolor='black', alpha=0.85)
        ax_plot.axhline(0, color='gray', linewidth=0.8, linestyle='--')
        ax_plot.set_title(f"Diem so 7 PC tai ({cx}, {cy})\n[{def_k}]", fontsize=10, fontweight='bold', color='#c0392b')
        ax_plot.set_xlabel("Thanh phan chinh (PCA Components)", fontweight='bold', fontsize=9)
        ax_plot.set_ylabel("Gia tri PC Score", fontweight='bold', fontsize=9)
        ax_plot.grid(axis='y', linestyle='--', alpha=0.5)
        
        for bar in bars:
            val = bar.get_height()
            ax_plot.annotate(f"{val:.2f}",
                             xy=(bar.get_x() + bar.get_width() / 2, val),
                             xytext=(0, 2 if val >= 0 else -8),
                             textcoords="offset points",
                             ha='center', va='bottom', fontsize=8)
                             
        ax_bottom.clear()
        if bottom_state['view'] == 'color' and 'color_image' in data_dict:
            ax_bottom.imshow(data_dict['color_image'])
            ax_bottom.set_title("Anh chup trai tao mo phang (Color Rotary Scan Unwrapped)", fontsize=10, fontweight='bold')
        elif 'svm_pred' in data_dict:
            ax_bottom.imshow(data_dict['svm_pred'])
            ax_bottom.set_title("Ban do phan loai khuyet tat tao SVM (SVM Defect Classification Map)", fontsize=10, fontweight='bold')
        ax_bottom.axis('off')
        
        fig.suptitle(f"Du lieu tao: 7 THANH PHAN CHINH THEO PCA [{mat_key.upper()}] | Dang xem: PC {pc_idx + 1}/7", 
                     fontsize=14, fontweight='bold', color='#2c3e50')
        fig.canvas.draw_idle()

    def render_hsi():
        b_idx = int(slider.val) - 1
        wl = data_dict['wavelengths'][b_idx]
        slice_2d = data_dict['hsi_data'][b_idx, :, :]
        
        ax_img1.clear()
        ax_img1.imshow(slice_2d, cmap=current_cmap)
        ax_img1.set_title(f"Anh sieu pho HSI o Band {b_idx + 1}/600\n[lambda = {wl:.1f} nm]", fontsize=10, fontweight='bold')
        ax_img1.axis('off')
        
        ax_img2.clear()
        norm_slice = (slice_2d - slice_2d.min()) / (slice_2d.max() - slice_2d.min() + 1e-8)
        rgb_disp = np.stack([norm_slice]*3, axis=-1)
        rgb_disp[data_dict['hsi_mask_norm'] > 0] = [0.1, 0.9, 0.2]
        rgb_disp[data_dict['hsi_mask_bruise'] > 0] = [0.95, 0.1, 0.1]
        ax_img2.imshow(rgb_disp)
        ax_img2.set_title("Vung chon Mask tren trai tao\n[Xanh: Lanh | Do: Giap/Thoi]", fontsize=10, fontweight='bold')
        ax_img2.axis('off')
        
        ax_img3.clear()
        ax_img3.imshow(data_dict['hsi_mask_obj'], cmap='gray')
        ax_img3.set_title("Vung Mask toan bo qua tao\n[mask_object]", fontsize=10, fontweight='bold')
        ax_img3.axis('off')
        
        ax_plot.clear()
        wl_arr = data_dict['wavelengths']
        cx, cy = last_click['x'], last_click['y']
        h, w = slice_2d.shape
        if 0 <= cy < h and 0 <= cx < w:
            pixel_spec = data_dict['hsi_data'][:, cy, cx]
            ax_plot.plot(wl_arr, pixel_spec, 'r-', linewidth=2.0, label=f'Pho pixel ({cx}, {cy})')
            ax_plot.axvline(wl, color='#2980b9', linestyle=':', linewidth=1.5, label=f'Band {b_idx + 1} ({wl:.0f}nm)')
            
        if data_dict['mean_norm_spec'] is not None:
            ax_plot.plot(wl_arr, data_dict['mean_norm_spec'], 'g--', linewidth=1.6, label='Pho TB: Vo lanh (Normal)')
        if data_dict['mean_bruise_spec'] is not None:
            ax_plot.plot(wl_arr, data_dict['mean_bruise_spec'], 'm--', linewidth=1.6, label='Pho TB: Vung giap (Bruise)')
            
        ax_plot.set_title("BANG DO PHO QUANG HOC THUC TE\n(Click vao tao de do pho tai diem)", fontsize=10, fontweight='bold', color='#16a085')
        ax_plot.set_xlabel("Buoc song Wavelength (nm)", fontweight='bold', fontsize=9)
        ax_plot.set_ylabel("He so phan xa (Reflectance)", fontweight='bold', fontsize=9)
        ax_plot.grid(True, linestyle='--', alpha=0.6)
        ax_plot.legend(loc='upper right', fontsize=8)
        
        ax_bottom.clear()
        if 'color_image' in data_dict:
            ax_bottom.imshow(data_dict['color_image'])
            ax_bottom.set_title("Anh tham chieu qua tao mo phang (Color Rotary Scan Unwrapped)", fontsize=10, fontweight='bold')
        ax_bottom.axis('off')
        
        fig.suptitle(f"Du lieu tao: BANG DO PHO SIEU PHO HSI (600 BANDS) | Band {b_idx + 1}/600 (lambda = {wl:.1f} nm)", 
                     fontsize=14, fontweight='bold', color='#16a085')
        fig.canvas.draw_idle()

    def update_all(val=None):
        nonlocal current_cmap
        current_cmap = radio_cmap.value_selected
        if "PCA" in radio_mode.value_selected:
            render_pca()
        else:
            render_hsi()

    def on_mode_change(label):
        if "PCA" in label:
            slider.label.set_text("Thanh phan PC: ")
            slider.valmin, slider.valmax, slider.valstep = 1, 7, 1
            slider.ax.set_xlim(1, 7)
            slider.set_val(1)
            btn_toggle.ax.set_visible(True)
        else:
            slider.label.set_text("Kenh Band (1-600): ")
            slider.valmin, slider.valmax, slider.valstep = 1, 600, 1
            slider.ax.set_xlim(1, 600)
            slider.set_val(250)
            btn_toggle.ax.set_visible(False)
        update_all()

    def on_click(event):
        if event.inaxes in [ax_img1, ax_img2, ax_img3]:
            if event.xdata is None or event.ydata is None:
                return
            last_click['x'] = int(round(event.xdata))
            last_click['y'] = int(round(event.ydata))
            if "PCA" in radio_mode.value_selected:
                if event.inaxes == ax_img1: last_click['defect'] = 'rusty'
                elif event.inaxes == ax_img2: last_click['defect'] = 'fungus_infection'
                elif event.inaxes == ax_img3: last_click['defect'] = 'insect_bite'
            update_all()

    def toggle_bottom(event):
        bottom_state['view'] = 'svm' if bottom_state['view'] == 'color' else 'color'
        update_all()

    slider.on_changed(update_all)
    radio_mode.on_clicked(on_mode_change)
    radio_cmap.on_clicked(update_all)
    btn_toggle.on_clicked(toggle_bottom)
    fig.canvas.mpl_connect('button_press_event', on_click)
    
    update_all()
    print("[*] Da khoi chay Viewer thanh cong.")
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Apple HSI & PCA Viewer")
    parser.add_argument('--test', action='store_true', help="Kiem tra tai du lieu ma khong mo GUI")
    args = parser.parse_args()

    print("=" * 65)
    print("  APPLE HSI & DEFECT VIEWER (PCA 7 PCs & 600-Band HSI Spectrum)")
    print("=" * 65)
    data = load_all_data()
    if not data:
        print("[!] Khong tim thay tap du lieu nao.")
        return
        
    print("[+] Da tai thanh cong tat ca cac tap du lieu.")
    if args.test:
        print("[*] Che do test thanh cong. Ket thuc.")
        return
        
    run_viewer(data)

if __name__ == '__main__':
    main()
