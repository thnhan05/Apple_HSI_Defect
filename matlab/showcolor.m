function rgbpicnormal = showcolor(data, r, g, b)

b_layer = data(:,:,b);
g_layer = data(:,:,g);
r_layer = data(:,:,r);

rgbpic(:,:,1) = r_layer;
rgbpic(:,:,2) = g_layer;
rgbpic(:,:,3) = b_layer;
maxval = max(max(max(rgbpic)));

rgbpicnormal = rgbpic/maxval;


end