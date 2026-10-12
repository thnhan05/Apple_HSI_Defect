function [pcimages,latent,coeff] = HSI_PCA(data2D,masklocate,s,comp)

[i_mask,~] = size(masklocate);

pcimages = zeros(s(1),s(2),comp);

[coeff,~,latent] = pca(data2D);
 
for component = 1:comp
     
     pc_vector = coeff(:,component);
     pc_Img_vector = zeros(i_mask,1);
 
     for i= 1:i_mask 
         
             pc_Img_vector(i) = dot(data2D(i,:),pc_vector);
             
     end
     
     pc_Img_vector = pc_Img_vector-min(pc_Img_vector);
     
     pc_Img = zeros(s(1),s(2));
     
    for i = 1:i_mask
        
        pc_Img(masklocate(i,1),masklocate(i,2)) = pc_Img_vector(i); 
        
    end
    
    pcimages(:,:,component) = pc_Img;
    
 end

end

