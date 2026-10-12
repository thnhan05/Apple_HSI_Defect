function bw = band_wave(data,f)

[~, ~, ks] = size(data);
bw = zeros(ks,2);

for i = 1:ks
    
    bw(i,1) = i;
    bw(i,2) = f.p(1)*i + f.p(2);

end

end

