import speedtest
import ssl
import pandas as pd
from pandas.io.json import json_normalize

#need a fake certificate
ssl._create_default_https_context = ssl._create_unverified_context

def test():
    s = speedtest.Speedtest()

    #List all servers
    s.get_servers()
    #get the closest one
    s.get_closest_servers(10)
    s.get_best_server()

    #check speed
    s.download()
    s.upload()

    res = s.results.dict()

    res_pd = pd.DataFrame(json_normalize(res))
    return res_pd


def main():
    # write to csv
    for i in range(5):
        print('Test #'+ str(i+1))
        p = test()
        p.to_csv('file.csv', mode='a', header=False,index = False)

if __name__ == '__main__':
    main()


