
% Description: this step creates mat file data including HSI data cube, mask_object, 
% bandwave, color image, black and white data. At the same time check the optimal mask of the fruit
% And can use this program to create a color image to select the common skin defect of the fruit


clear all;
clc;

% Initial parameter and value

model = 'SVM_model_mask_v10.mat';
k = 38:489; % v10
% k = 345:796; % v10e
se = strel('disk',10);


%--------------------------------------------------------------------------

file = 'E:\PQT\paper\MDPI\HSI_online\linear_scan_V10.xlsx';
[~,~,raw] = xlsread(file,'Sheet1');

[ra,~] = size(raw);
format = '*.tiff';
coef = load('factor_aca1920_155um_03_2020.mat');

%--------------------------------------------------------------------------

for i = 2:2%ra-1
    
    data = [];
    
    if raw{i,7} == 1 % The value of Select in excel file that can only be checked after fruits with general skin defects 
        % are selected completely
    
        % combine HSI data from images

        srcFiles = dir(strcat(raw{i,2},'\',format));
        isize = length(srcFiles);
        filename = strcat(raw{i,2},'\',srcFiles(1).name);
        [ksize, jsize] = size(imread(filename));

        HSIdata = zeros(jsize, isize, ksize);

        for j = 1:isize

            % read line scan spectral files and combine
            filename = strcat(raw{i,2},'\',srcFiles(j).name);
            % note: offset the 12 bit image stored in 16 bit format and find normalized
            % The resolution of the camera is 2^12 
            scanlinemat = (double(imread(filename) - (2^15 - 1)))/(2^12 - 1);
            scanlinemat = scanlinemat';
            HSIdata(:,j,:) = scanlinemat(1:jsize,1:ksize);      

        end

        waveband = band_wave(HSIdata,coef);

        % Resize data   

        str = raw{i,5};
        x = sscanf(str,'%d:%d');
        str = raw{i,6};
        y = sscanf(str,'%d:%d');
        HSIdata_f1 = HSIdata(y(1):y(2),x(1):x(2),:);

        % Average black, white images    

        path = strcat(raw{i,3},'white','\');
        white = averageimage(path,y);   
        path = strcat(raw{i,3},'black','\');    
        black = averageimage(path,y);

        nonhsidata = raw_2_filter_calib(HSIdata_f1,'v10',0,1,'loess',30,black,white);
        hsidata = raw_2_filter_calib(HSIdata_f1,'v10',1,1,'loess',30,black,white);

% Step 1: Create RGB image to select fruits with common skin defects. 
% At this step Select in excel file should be all equal to 1    

        color = showcolor(nonhsidata, 239, 155, 95); % 622 nm; 530 nm; 465 nm
        color = color*1.5; 
        color = im2uint8(color);

        fileimage = strcat(raw{i,8},raw{i,10},raw{i,4},'.bmp');
%         imwrite(color,fileimage);
        
% Step 2: Create mask object and erode from selected fruits       
        
        [mask_object, ~] = predict_mask(hsidata,k,model,se);
        mask7 = mask_object;
        filename = strcat(raw{i,8},raw{i,10},raw{i,4},'.png');
        imwrite(mask_object,filename);
               
% Step 3: Save raw data        
    
        data.HSIdata = nonhsidata;
        data.mask.mask_object = mask_object;
        data.bandwave = waveband;
        data.white = white;
        data.black = black;
        data.color = color;
        filename = strcat(raw{i,8},raw{i,9},raw{i,4},'.mat');
        
%         save(filename,'data','-v7.3');
            
    end   
    
end