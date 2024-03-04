import os
import hashlib
import time
import shutil
import argparse




#check_file: compares 2 files and returns True if equal or False if different       

def check_file(source_path, replica_path):

    with open(source_path, 'rb') as source_file, open(replica_path, 'rb') as replica_file:
        return hashlib.md5(source_file.read()).hexdigest() == hashlib.md5(replica_file.read()).hexdigest()
            

#check_folder: compares 2 folders and returns True if equal or False if different
    
def check_folder(source, replica, log_path):
    source_files = os.listdir(source)
    replica_files = os.listdir(replica)
     
    for file in source_files:

        #check if the file in source exists in replica 

        if file in replica_files:

            if os.path.isdir(replica+'/'+file):

                check_folder(source+'/'+file, replica+'/'+file, log_path)


            elif not check_file(source+'/'+file, replica+'/'+file):

                #contents are different

                shutil.copy(source+'/'+file, replica+'/'+file)
                log(f'modified {replica +'/'+ file}',log_path)
        
        else:

            #creates file
            

            if os.path.isdir(source+'/'+file):
                
                shutil.copytree(source+'/'+file, replica+'/'+file)
                log(f'created directory {replica +'/'+ file}',log_path)
            else:
                shutil.copy(source+'/'+file, replica+'/'+file)
                log(f'created {replica +'/'+ file}',log_path)
        
    for file in replica_files:

        #file from replica does not exist in source

        if file not in source_files:

            #removes file
            if os.path.isdir(replica+'/'+file):
                shutil.rmtree(replica+'/'+file)
                log(f'removed directory {replica +'/'+ file}',log_path)

            else:
                os.remove(replica+'/'+file)
                log(f'removed {replica +'/'+ file}',log_path)




        
#log: File creation, modification and removal are logged and printed

def log(logtext,log_path):

    log_time = time.strftime("%d/%m/%Y - %H:%M:%S", time.localtime())

    with open(log_path, 'a') as log_file:
        log_file.write('[' + log_time + '] - ' + logtext + '\n')

    print('[' + log_time + '] - ' + logtext + '\n')

def foldersync(source, replica, log_path, period):

    #check if replica exists

    if not os.path.isdir(replica):

        #creates replica folder if it doesn't 

        os.makedirs(replica)

        log('Replica folder created',log_path)
        print('Replica folder created')

    #check if source exists

    if not os.path.isdir(source):

        #terminates porgram if it doesn't

        log('Source folder not found',log_path)
        return
        
    log('folder synchronization started',log_path)

    while True:
        try:
            check_folder(source,replica, log_path)
            print('Updated!....Ctrl+C to exit\n')
            time.sleep(period)

        except KeyboardInterrupt:

            #if interrupted exits

            log('folder synchronization finished', log_path)
            print("Exiting")
            return
        


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--source', type=str, default="source", help='Path to the Source folder')
    parser.add_argument('--replica', type=str, default="replica", help='Path to the Replica folder')
    parser.add_argument('--log_path', type=str, default='logfile.txt', help='Path to the Log file')
    parser.add_argument('--period', type=int, default=30, help='update period')

    args = parser.parse_args()

foldersync(args.source, args.replica, args.log_path, args.period)