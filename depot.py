#!/usr/bin/env python

##Generating a new lager
depot =[ #type 1
        {'x':10, 'y':0, 'z':0, 'typ':1, 'rot':0},
        {'x':10, 'y':1, 'z':0, 'typ':1, 'rot':0},
        {'x':10, 'y':2, 'z':0, 'typ':1, 'rot':0},
        {'x':10, 'y':3, 'z':0, 'typ':1, 'rot':0},
        {'x':9, 'y':0, 'z':0, 'typ':1, 'rot':0},
        {'x':9, 'y':1, 'z':0, 'typ':1, 'rot':0},
        {'x':9, 'y':2, 'z':0, 'typ':1, 'rot':0},
        {'x':9, 'y':3, 'z':0, 'typ':1, 'rot':0},
        {'x':8, 'y':0, 'z':0, 'typ':1, 'rot':0},
        {'x':8, 'y':1, 'z':0, 'typ':1, 'rot':0},
        {'x':8, 'y':2, 'z':0, 'typ':1, 'rot':0},
        {'x':8, 'y':3, 'z':0, 'typ':1, 'rot':0},
        {'x':10, 'y':0, 'z':1, 'typ':1, 'rot':0}, #13
        {'x':10, 'y':1, 'z':1, 'typ':1, 'rot':0},
        {'x':10, 'y':2, 'z':1, 'typ':1, 'rot':0},
        {'x':10, 'y':3, 'z':1, 'typ':1, 'rot':0},
        {'x':9, 'y':0, 'z':1, 'typ':1, 'rot':0},
        {'x':9, 'y':1, 'z':1, 'typ':1, 'rot':0},
        {'x':9, 'y':2, 'z':1, 'typ':1, 'rot':0},
        {'x':9, 'y':3, 'z':1, 'typ':1, 'rot':0}, #20
        {'x':8, 'y':0, 'z':1, 'typ':1, 'rot':0},
        {'x':8, 'y':1, 'z':1, 'typ':1, 'rot':0},
        {'x':8, 'y':2, 'z':1, 'typ':1, 'rot':0},
        {'x':8, 'y':3, 'z':1, 'typ':1, 'rot':0},
        {'x':10, 'y':0, 'z':2, 'typ':1, 'rot':0},
        {'x':10, 'y':1, 'z':2, 'typ':1, 'rot':0},
        {'x':10, 'y':2, 'z':2, 'typ':1, 'rot':0},
        {'x':10, 'y':3, 'z':2, 'typ':1, 'rot':0},
        {'x':9, 'y':0, 'z':2, 'typ':1, 'rot':0},
        {'x':9, 'y':1, 'z':2, 'typ':1, 'rot':0}, #30
        {'x':9, 'y':2, 'z':2, 'typ':1, 'rot':0},
        {'x':9, 'y':3, 'z':2, 'typ':1, 'rot':0},
        {'x':8, 'y':0, 'z':2, 'typ':1, 'rot':0},
        {'x':8, 'y':1, 'z':2, 'typ':1, 'rot':0},
        {'x':8, 'y':2, 'z':2, 'typ':1, 'rot':0},
        {'x':8, 'y':3, 'z':2, 'typ':1, 'rot':0},
        {'x':10, 'y':0, 'z':3, 'typ':1, 'rot':0},
        {'x':10, 'y':1, 'z':3, 'typ':1, 'rot':0},
        {'x':10, 'y':2, 'z':3, 'typ':1, 'rot':0},
        {'x':10, 'y':3, 'z':3, 'typ':1, 'rot':0}, #40
        {'x':9, 'y':0, 'z':3, 'typ':1, 'rot':0},
        {'x':9, 'y':1, 'z':3, 'typ':1, 'rot':0},
        {'x':9, 'y':2, 'z':3, 'typ':1, 'rot':0},
        {'x':8, 'y':0, 'z':3, 'typ':1, 'rot':0},
        {'x':8, 'y':1, 'z':3, 'typ':1, 'rot':0},
        {'x':8, 'y':2, 'z':3, 'typ':1, 'rot':0}, #46
        
        #type 2
        {'x':6, 'y':3, 'z':0, 'typ':2, 'rot':0},
        {'x':6, 'y':3, 'z':1, 'typ':2, 'rot':0},
        {'x':6, 'y':3, 'z':2, 'typ':2, 'rot':0},
        {'x':6, 'y':3, 'z':3, 'typ':2, 'rot':0}, #4
        
        #type 3
        {'x':6, 'y':0, 'z':0, 'typ':3, 'rot':0},
        {'x':6, 'y':1, 'z':0, 'typ':3, 'rot':0},
        {'x':6, 'y':0, 'z':1, 'typ':3, 'rot':0},
        {'x':6, 'y':1, 'z':1, 'typ':3, 'rot':0},
        {'x':6, 'y':0, 'z':2, 'typ':3, 'rot':0},
        {'x':6, 'y':1, 'z':2, 'typ':3, 'rot':0},
        {'x':6, 'y':0, 'z':3, 'typ':3, 'rot':0}, #3
        
        #type 4
        {'x':4, 'y':3, 'z':0, 'typ':4, 'rot':0},
        {'x':4, 'y':3, 'z':1, 'typ':4, 'rot':0}, #2
        
        #type 5
        {'x':6, 'y':5, 'z':0, 'typ':5, 'rot':0},
        {'x':6, 'y':5, 'z':1, 'typ':5, 'rot':0},
        {'x':6, 'y':5, 'z':2, 'typ':5, 'rot':0},
        {'x':6, 'y':5, 'z':3, 'typ':5, 'rot':0}, #4
        
        #type 6
        {'x':4, 'y':5, 'z':0, 'typ':6, 'rot':0},
        {'x':4, 'y':5, 'z':1, 'typ':6, 'rot':0},
        {'x':4, 'y':5, 'z':2, 'typ':6, 'rot':0},
        {'x':4, 'y':5, 'z':3, 'typ':6, 'rot':0}, #6
        
        #tpye 7
        {'x':4, 'y':0, 'z':0, 'typ':7, 'rot':0},
        {'x':4, 'y':1, 'z':0, 'typ':7, 'rot':0},
        {'x':4, 'y':0, 'z':1, 'typ':7, 'rot':0},
        {'x':4, 'y':1, 'z':1, 'typ':7, 'rot':0},
        {'x':4, 'y':0, 'z':2, 'typ':7, 'rot':0},
        {'x':4, 'y':0, 'z':3, 'typ':7, 'rot':0}, #6
        
        #type 8
        {'x':2, 'y':0, 'z':0, 'typ':8, 'rot':0},
        {'x':2, 'y':1, 'z':0, 'typ':8, 'rot':0},
        {'x':2, 'y':0, 'z':1, 'typ':8, 'rot':0},
        {'x':2, 'y':1, 'z':1, 'typ':8, 'rot':0},
        {'x':2, 'y':1, 'z':1, 'typ':8, 'rot':0},
        {'x':2, 'y':0, 'z':3, 'typ':8, 'rot':0}, #6
        
        #type 9
        {'x':2, 'y':3, 'z':0, 'typ':9, 'rot':0},
        {'x':2, 'y':3, 'z':1, 'typ':9, 'rot':0},
        {'x':2, 'y':3, 'z':2, 'typ':9, 'rot':0},
        {'x':2, 'y':3, 'z':3, 'typ':9, 'rot':0}, #4
        
        #type 10
        {'x':2, 'y':5, 'z':0, 'typ':10, 'rot':0},
        {'x':2, 'y':5, 'z':1, 'typ':10, 'rot':0},
        {'x':2, 'y':5, 'z':2, 'typ':10, 'rot':0},
        {'x':2, 'y':5, 'z':3, 'typ':10, 'rot':0}, #4
        
        #type 11
        {'x':10, 'y':5, 'z':0, 'typ':11, 'rot':0},
        {'x':9, 'y':5, 'z':0, 'typ':11, 'rot':0},
        {'x':8, 'y':5, 'z':0, 'typ':11, 'rot':0},
        {'x':10, 'y':5, 'z':1, 'typ':11, 'rot':0},
        {'x':9, 'y':5, 'z':1, 'typ':11, 'rot':0},
        {'x':8, 'y':5, 'z':1, 'typ':11, 'rot':0},
        {'x':10, 'y':5, 'z':2, 'typ':11, 'rot':0},
        {'x':9, 'y':5, 'z':2, 'typ':11, 'rot':0},
        {'x':8, 'y':5, 'z':2, 'typ':11, 'rot':0},
        {'x':10, 'y':5, 'z':3, 'typ':11, 'rot':0},
        {'x':9, 'y':5, 'z':3, 'typ':11, 'rot':0},
        {'x':8, 'y':5, 'z':3, 'typ':11, 'rot':0},  #12
        
        #type 12
        {'x':0, 'y':0, 'z':0, 'typ':12, 'rot':0},
        {'x':0, 'y':1, 'z':0, 'typ':12, 'rot':0},
        {'x':0, 'y':0, 'z':1, 'typ':12, 'rot':0},
        {'x':0, 'y':0, 'z':2, 'typ':12, 'rot':0},
        {'x':0, 'y':0, 'z':3, 'typ':12, 'rot':0}, #5
        
        #type 13
        {'x':0, 'y':3, 'z':0, 'typ':13, 'rot':0},
        {'x':0, 'y':3, 'z':1, 'typ':13, 'rot':0}, #2
        ]

c=0
for i in depot:
    c+=1
print c

demo_anlage = [{'x':13, 'y':0, 'z':0, 'typ':1, 'rot':0},
               {'x':13, 'y':0, 'z':1, 'typ':2, 'rot':3},
               {'x':14, 'y':0, 'z':0, 'typ':2, 'rot':0},
               ]

def calculate_mazine(lager, anlage):
    '''Calculates the new anlage
    '''
    final=[]
    for i in lager:
        final.append(i)
    
    c=0
    for i in lager:
        c+=1
    print 'alle wrfel1:', c
    
    for cube in anlage:
        typ=cube['typ']
        
        types=[]
        for cu in lager:
            if cu['typ']==typ:
                types.append(cu)
        print len(types), "of", typ
        
        #highest cube in types
        z=0
        ind=-1
        for cu in types:
            if cu['z']>z:
                ind=types.index(cu,)
        if ind==-1:
            print "No highest cube found"
            return False
        print 'Final cube', types[ind]
        
        lager.remove(types[ind])
        final.remove(types[ind])
        final.append(cube)
            
    c=1
    for i in final:
        print c, i
        c+=1
    
    return final
    
    
        
        
        

if __name__ == '__main__':
    calculate_mazine(depot, demo_anlage)
    