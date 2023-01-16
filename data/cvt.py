import json
import pandas as pd

def main():
    script = pd.DataFrame()
    for task in ['test','train','valid']:
        with open(f'/Users/sabin/Documents/GitHub/podcast-gpt/data/{task}-transcripts-aligned.json') as f:
            data = json.load(f)
        
        df= pd.DataFrame(columns=data[next(iter(data.keys()))][0].keys()).astype({"has_q":bool, "ends_q":bool})
        for key in data.keys():
            temp = pd.DataFrame(data[key]).astype({"has_q":bool, "ends_q":bool})
            df = pd.concat([df, temp])
        
        script = pd.concat([script, df])

    script.to_csv('/Users/sabin/Documents/GitHub/podcast-gpt/data/script.csv', index=False)


if __name__=="__main__":
    main()