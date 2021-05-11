

params={}

def replace_value_params(params,line):
    for f_key, f_value in params.items():
        if f_key in line:
            line = line.replace(f_key, f_value)
    return line

def main():
    try:
        with open("Test_GCP_Migration.csv", "r") as f:
            lines = f.readlines()
    except Exception as e:
        print(e)
        raise
    else:
        f.close()
    
    try:
        cols=lines[0].strip().split(",")
        values=lines[1].strip().split(",")
        params=dict(zip(cols,values))

        mds_rds="gcloud database-migration connection-profiles create postgresql RdsId --region=Location --password=ReplicationPassword  --username=ReplicationUsername --display-name=RdsName --host=EndpointAddress --port=Port"

        mds_cloudsql="gcloud database-migration connection-profiles create cloudsql ClouqSqld --region=Location --display-name=CloudSqlName --database-version=Version --tier=Tier --source-id=RdsId"

        mds_job="gcloud database-migration migration-jobs create JobId --region=Location --display-name=JobName --source=RdsId  --destination=ClouqSqld --type=Type"

        mds_job_run="gcloud database-migration migration-jobs start JobId --region=Location"

        mds_p1=replace_value_params(params,mds_rds)
        mds_p2=replace_value_params(params,mds_cloudsql)
        mds_p3=replace_value_params(params,mds_job)
        mds_p4=replace_value_params(params,mds_job_run)
        
        print(mds_p1)
        print(mds_p2)
        print(mds_p3)
        print(mds_p4)
        
    except Exception as e:
        print(e)
        raise

if __name__ == "__main__":
    main()
