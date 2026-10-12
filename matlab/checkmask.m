%load('D:\pyworkdata\avocado_new.mat')
%load('D:\pyworkdata\avocado_size1.mat')
%load('D:\pyworkdata\avocado_size2.mat')
load('D:\HSIdata19.mat')

%load('D:\pyworkdata\HSIdata19.mat')
%load('D:\pyworkdata\HSIdata20.mat')

layer=450
show_layer=hsidata.data(:,:,layer);
figure
imagesc(show_layer)
colormap gray

current_mask_object=hsidata.mask_object;
mask_edge_object = edge(current_mask_object,'log');
figure
imshow(current_mask_object)
figure
imshow(mask_edge_object)

%figure
%imshow(current_mask_object)

current_mask_normal=hsidata.mask_normal;
mask_edge_normal = edge(current_mask_normal,'log');
figure
imshow(mask_edge_normal)

current_mask_bruise=hsidata.mask_bruise;
mask_edge_bruise = edge(current_mask_bruise,'log');
figure
imshow(mask_edge_bruise)




[isize jsize]=size(mask_edge_normal)
show_layer_mask=show_layer;

for i= 1:isize
    for j=1:jsize
        if mask_edge_object(i,j)==1
            show_layer_mask(i,j)=1;
        end
        if mask_edge_normal(i,j)==1
            show_layer_mask(i,j)=1;
        end
        if mask_edge_bruise(i,j)==1
            show_layer_mask(i,j)=0;
        end
        
        
    end
end
figure
imagesc(show_layer_mask);
colormap gray;




