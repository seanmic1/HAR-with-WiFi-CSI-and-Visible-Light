import pandas as pd
import glob
import datetime as dt
import math

def combine_data():
    # get file names
    csi_path = "csi_data/*.csv"
    light_path = "light_data/*.csv"

    csi_fnames = glob.glob(csi_path)
    light_fnames = glob.glob(light_path)

    # convert light data from long to wide
    # for i in range(len(light_fnames)):
    for i in range(1):

        # read csv
        light_df = pd.read_csv(light_fnames[i],header=None)

        print("Reading", light_fnames[i])
        
        # get min and max time
        min_time = dt.datetime.strptime(light_df.iloc[0][0],"%Y-%m-%d %H:%M:%S")
        max_time = dt.datetime.strptime(light_df.iloc[-1][0],"%Y-%m-%d %H:%M:%S")

        # removing one second to account for delay
        start_time = min_time - dt.timedelta(seconds=1)

        # make buckets of 100 ms in csv
        time_buckets = []

        while start_time < max_time:

            time_buckets.append(start_time.strftime("%Y-%m-%d %H:%M:%S.%f"))

            # new_df[j]["time"] = start_time.strftime("%Y-%m-%d %H:%M:%S.%f")

            start_time = start_time + dt.timedelta(milliseconds=100)

        # make new dataframe with buckets and empty data
        new_df = pd.DataFrame({
            "time": time_buckets,
            "1": [None] * len(time_buckets),
            "2": [None] * len(time_buckets),
            "3": [None] * len(time_buckets),
            "4": [None] * len(time_buckets),
            "5": [None] * len(time_buckets),
            "6": [None] * len(time_buckets),
            "7": [None] * len(time_buckets),
            "8": [None] * len(time_buckets),
            "9": [None] * len(time_buckets),
        })

        # convert from long to wide using df.pivot()
        pivoted = light_df.pivot(index=1, columns=2, values=3)

        # put pivoted data into new dataframe
        for index, row in pivoted.iterrows():
            
            # round time to know the bucket
            rounded_time = dt.datetime.strptime(str(row.name), "%Y-%m-%d %H:%M:%S.%f")
            rounded_time = rounded_time.replace(microsecond=(rounded_time.microsecond // 100000) * 100000)

            # get sensor number
            for l in range(len(row.values)):
                if pd.notnull(row.values[l]):
                    sensor_number = l

            new_df.loc[new_df['time'] == rounded_time.strftime("%Y-%m-%d %H:%M:%S.%f"), str(sensor_number)] = row.values[sensor_number]

        # combine with CSI data

        # read CSI data file
        print("Reading", csi_fnames[i])

        csi_df = pd.read_csv(csi_fnames[i])

        print(csi_df)



        # export to csv

        # filename = light_fnames[i][11:-4] + "_wide.csv"

        # new_df.to_csv("temp_wide_light_data/"+filename, index=False)
    
if __name__ == "__main__":
    combine_data()







