import mgrs 

def mgrs_to_lat_long(mgrs_grid):

    m = mgrs.MGRS()
    d = m.toLatLon(mgrs_grid)

    return d


print(mgrs_to_lat_long("39sxs2983701890"))