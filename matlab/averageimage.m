function out = averageimage(path,range)

if (length(path) == 1)

%     clc;
%     temp = 'Please Load images';
%     set(info,'String',temp);

else

    format = '*.tiff';
    srcFiles = dir(strcat(path,format));
    filename = strcat(path,srcFiles(1).name);
    temp = imread(filename)';
%     temp = temp(range(1):range(2),:);
    [re,b] = size(temp);
    out = zeros(re,b);

    for i = 1:length(srcFiles)

        filename = strcat(path,srcFiles(i).name);
        temp = (double(imread(filename) - (2^15 - 1)))/(2^12 - 1);
        temp = temp';
%         temp = temp(range(1):range(2),:);
        out = out + temp;

    end

    out = out/i;

end

end

