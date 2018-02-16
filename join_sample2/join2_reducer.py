prev_show          = " "                #initialize previous show to blank string

is_abc             = 0 #indicate shows on abc
viewer_total         = 0 #sum viewers
# see https://docs.python.org/2/tutorial/datastructures.html for list details

line_cnt           = 0  #count input lines
curr_show          = " "
for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list
    line_cnt   = line_cnt+1     

    #note: for simple debugging use print statements, ie:  
    curr_show  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item

    #-----------------------------------------------------
    # Check if its a new show and not the first line 
    #   (b/c for the first line the previous word is not applicable)
    #   if so then print out list of dates and counts
    #----------------------------------------------------
    if curr_show != prev_show:

        # -----------------------     
	#now write out the join result, but not for the first line input
        # -----------------------
        if line_cnt>1 and is_abc==1:
	    print('{0} {1}'.format(prev_show,viewer_total))
            #now reset lists
	is_abc = 0
        viewer_total = 0
        prev_show = curr_show  #set up previous show for the next set of input lines

	
    # ---------------------------------------------------------------
    #whether or not the join result was written out, 
    #   now process the curr show    
  	
    #determine if its from file <show, viewer_count> or <show, channel>
    # and add up the total viewers
    # ---------------------------------------------------------------
    if value_in == 'ABC': 
        
        is_abc = 1

    else:

        viewer_total += int(value_in)

# ---------------------------------------------------------------
#now write out the LAST join result
# ---------------------------------------------------------------
print('{0} {1}'.format(curr_show,viewer_total))
