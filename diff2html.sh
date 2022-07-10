#https://stackoverflow.com/questions/25520709/html-conversion-with-vimdiff-in-shell-script

vimdiff file1 file2 -c TOhtml -c  'w! diff_output.html' -c 'qa!'
vimdiff -c "set foldlevel=9999" input.nml ../rrfs_a -c TOhtml -c 'w! diff_test.html' -c 'qa!'

