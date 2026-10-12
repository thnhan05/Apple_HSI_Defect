function [bwe, layer] = predict_mask(HSIdata,range,name,se)

load(name,'model');
[is,js,ks] = size(HSIdata);

% axes(s1);
% axes(s2);

for i = 1:js
    
   simage = reshape(HSIdata(:,i,:),[is ks]) ;
   simage = simage(:,range);
      
   temp = predict(model,simage);
   temp1 = temp;
   temp(end) = 0;
   
   if i == 1
       
        temp2 = simage(:,200);
        ypredict = temp;
        bwo = temp1;
    
   elseif i > 1
      
        temp2 = [temp2 simage(:,200)];
        ypredict = [ypredict temp];
        bwo = [bwo temp1];
       
   end
   
   bwe = imerode(ypredict,se);  
%    bwe = ypredict;
%    imagesc(s1,temp2);
%    colormap(s1,'gray');
%    axis image;
%    
%    imagesc(s2,bwe);
%    colormap(s2,'gray');
%    axis image;
%    pause(0.05);
      
end

layer = temp2;

end