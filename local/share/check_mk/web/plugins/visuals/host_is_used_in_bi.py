#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

class BIHostIsUsedFilter(FilterTristate):
    def __init__(self):        
        FilterTristate.__init__(self, "aggr_host_used", _("Used in BI aggregate"), "host", None)    
    
    def filter(self, infoname):        
        return ""    
        
    def filter_table(self, rows):        
        current = self.tristate_value()        
        if current == -1:            
            return rows        
        new_rows = []        
        for row in rows:            
            is_part = bi.is_part_of_aggregation(                   
                "host", row["site"], row["host_name"], row["host_name"])            
            if (is_part and current == 1) or \               
                (not is_part and current == 0):                
                new_rows.append(row)        
        return new_rows
        
declare_filter(299, BIHostIsUsedFilter())
