function [str_result] = palindrom(x)
    x = lower(x);
    len = length(x);
    leftBound = floor(len / 2);
    rightBound = ceil(len / 2) + 1;
    result = all(x(1:leftBound) == flip(x(rightBound:len)));
    
    if result
        str_result = 'ano';
    else
        str_result = 'ne';
    end
end