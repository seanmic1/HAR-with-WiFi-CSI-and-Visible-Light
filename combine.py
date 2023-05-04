import pandas as pd
import glob

# get file names
csi_path = "csi_data/*.csv"
light_path = "light_data/*.csv"

csi_fnames = glob.glob(csi_path)
light_fnames = glob.glob(light_path)

# convert light data from long to wide
for i in range(len(light_fnames)):

    if (i == 1):
        light_df = pd.read_csv(light_fnames[i],header=None)
        # convert from long to wide using df.pivot()
        pivoted = light_df.pivot(index=1, columns=2, values=3)

        # make buckets for per second


        print(pivoted)








