function hsidata_calib = raw_2_filter_calib(hsidata,machinename,enablefilter,enablecalib,modefilter,numfilter,black,white)

% machinename - v10 or v10e
% filter smoothdata funciton


% filter
        
[is,js,ks] = size(hsidata);
hsidata_filter = zeros(is,js,ks);
hsidata_calib = zeros(is,js,ks);

if enablefilter == 1

    switch machinename

        case 'v10'

            for i = 1:js

               temp = reshape(hsidata(:,i,:),[is ks]);
               tempf = zeros(is,ks);

               for j = 1:is

                  tempf(j,:) = smoothdata(temp(j,:),modefilter,numfilter);                      

               end

               hsidata_filter(:,i,:) = tempf;

            end

        case 'v10e'

            for i = 1:js

               temp = reshape(hsidata(:,i,:),[is ks]);
               tempf = zeros(is,ks);

               for j = 1:is

                  tempf(j,:) = smoothdata(temp(j,:),modefilter,numfilter);                      

               end

               hsidata_filter(:,i,:) = tempf;

            end

    end
    
else
    
    hsidata_filter = hsidata;

end

% calibrate

if enablecalib == 1

    switch machinename

        case 'v10'

            for i = 1:js

                s = reshape(hsidata_filter(:,i,:),[is ks]);
                ref = (s - black) ./ (white - black);
                hsidata_calib(:,i,:) = ref;

            end

        case 'v10e'

            for i = 1:is

                s = reshape(hsidata_filter(i,:,:),[js ks]);
                ref = (s - black) ./ (white - black);
                hsidata_calib(i,:,:) = ref;

            end

    end
    
else
    
    hsidata_calib = hsidata_filter;

end

end

