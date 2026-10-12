clear all;
close all;
clc

load('vis_nir.mat');
comp = 7;

for i = 1:comp
   
   pc_rusty = rusty(:,:,i);
   pc_insect = insect_bite(:,:,i);
   pc_fungus = fungus_infection(:,:,i);
   
   figure(i);   
   subplot(1,3,1);
   colormap('gray');
   imagesc(pc_rusty);
   axis image; 
   axis off;
   
   subplot(1,3,2);
   colormap('gray');
   imagesc(pc_fungus);
   axis image; 
   axis off;
   
   subplot(1,3,3);
   colormap('gray');
   imagesc(pc_insect);
   axis image; 
   axis off;   
   
end