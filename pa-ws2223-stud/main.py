def main():
    # setting hdf5 file's path (with name)
    data_file = "../project/data/data_230209_GdD_PA3_Datensatz_Kennfeldmessung_Exzenterschneckenpumpe_Sirupmischanlage_Logan.hdf5"
    #setting array which keeps speeds
    speeds = ['540','1400','300']
    #setting array which keeps indexes
    index = ['deg16.5' , 'deg18' , 'deg24' , 'deg36' , 'deg60']
    #setting array with features of interest
    features_of_interest=['cyan_dp','cyan_q']
    pass


if __name__ == "__main__":
    main()
