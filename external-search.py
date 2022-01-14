#external search of the hdd
#written by xishan lone
#all import files are here please check if you have all installed
#for pickle please insert this in cmd pip install pickle5
import os
import time
from datetime import datetime
import pickle

# code snippet to retive the fielpath
#input is filename
#start search from the root directory
# this is the naive method of retrival

#path_1 signifies the root directory
path_1=r'C:/'
def naive_search():
    file_list=[]
    print('Enter the file name and its extension eg=filename.ext')
    file_name=input(str)
    path_dictionary={}
    starting_time=datetime.now()
    #start the topdown traversal of the directory
    for root, dirs, files in os.walk(path_1):
        for file in files:
            if file_name==file:
                file_list.append(root)
    path_dictionary[file_name]=file_list
    completion_time=datetime.now()
    print("The path for : ",file_name, " : are/is : ",path_dictionary[file_name])
    print("time taken is: ",completion_time-starting_time)



# code to put the whole index in the dictionary
#key=filename, value=path to file


index_dictionary={}
def create_index():
    path_list=[]
    for root, dirs, files in os.walk(path_1):
        for file in files:
            if file not in index_dictionary:
                path_list.append(root)
                index_dictionary[file]=path_list
                path_list=[]
            else:
                index_dictionary[file].append(root)
    return index_dictionary

#get the path of the current working directory
def hash_approach():
    path=os.getcwd()

    if os.path.isfile("paths.pickle"):
        # if the pickle file already exists in cwd
        print("Index file exists do you want to re-index if yes press [y/Y]")
        answer=input(str)
        #if you want to create index again press y
        if answer=='y' or answer=='Y':
            index_dictionary=create_index()
            with open('paths.pickle', 'wb') as index:
                pickle.dump(index_dictionary, index, protocol=pickle.HIGHEST_PROTOCOL)
        else:
            #index already create just load the pickle file
            #unserilasise and load data back again
            with open('paths.pickle', 'rb') as index:
                index_dictionary=pickle.load(index)
        # print(index_dictionary)
            
    else:
        #searilise data and save it to a pickle file
        index_dictionary=create_index()
        with open('paths.pickle', 'wb') as index:
            pickle.dump(index_dictionary, index, protocol=pickle.HIGHEST_PROTOCOL)


    # for xi_shan in index_dictionary:
    #     print(index_dictionary[xi_shan])
    # take input for the dictionary to see the output paths

    print("Enter the file name .extension")
    search_filename=input(str)
    #timer start to check the retival speed
    starting_time=datetime.now()

    if search_filename in index_dictionary:
        print("the path for : ", search_filename, " : is/are : ", index_dictionary[search_filename])
    else:
        print("Please check the file name or the file does not exist")

    completion_time=datetime.now()
    #timer stops when retrival finishes
    print("using dictionary the retrival time of the file path is : ",completion_time-starting_time)

if __name__=='__main__':
    print("choose the method of search 1=naive and 2=fast search")
    ans=input()
    if ans=='2':
        hash_approach()
    elif ans=='1':
        naive_search()
    else:
        print('Enter a valid choice')
    
