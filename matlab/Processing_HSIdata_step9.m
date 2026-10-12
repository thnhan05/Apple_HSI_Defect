
% Description: this step is to apply PCA method for each fruit

clear all;
close all;
clc

path = 'E:\PQT\paper\MDPI\HSI_online\new_2020\data4train\Vis_nir\';
format = '*.mat';
srcFiles = dir(strcat(path,format));
comp = 8;

path1 = 'E:\PQT\paper\MDPI\HSI_online\new_2020\data4train\pca_eachfruit\';

for i = 1:1%length(srcFiles)
    
    filename = strcat(path,srcFiles(i).name);
    load(filename,'predictdata','predictdataf','mask_object','predictlocate','bandwave');
    
    s = size(mask_object);
    masklocate = predictlocate(:,1:2);
    
    [pcimages,latent,coeff] = HSI_PCA(predictdata,masklocate,s,comp);
    [pcimagesf,latentf,coefff] = HSI_PCA(predictdataf,masklocate,s,comp);
    
    name = srcFiles(i).name;
    name = name(1:length(name)-10);
    
    for j = 1:comp        
            
        temp = pcimages(:,:,j);
        tempf = pcimagesf(:,:,j);
        level = 255/max(max(temp));
        levelf = 255/max(max(tempf));
        
        temp = uint8(temp*level);
        tempf = uint8(tempf*levelf);
                
%         file = strcat(path1,'nonfilter\',name,'_PC',num2str(j),'.bmp');
%         imwrite(temp,file);
        
%         file = strcat(path1,'filter\',name,'_PC',num2str(j),'.bmp');
%         imwrite(tempf,file);
            
    end
        
%     file = strcat(path1,name,'_pca.mat');
%     save(file,'pcimages','coeff','pcimagesf','coefff','bandwave','latent','latentf');
    
end