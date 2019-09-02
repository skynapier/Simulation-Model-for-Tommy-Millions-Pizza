#author tian
import datetime

def load_data(data_dir):
    '''
    load the whole data set with txt file
    :param data_dir:
    :return:
    a array include each line in txt file
    '''
    ret = []
    with open(data_dir, 'r') as d_f:
        for line in d_f:
            line = line.strip().split()
            ret.append(line)
    return ret

def split_data_set(data_set):
    '''
    due to our data collect in different days but in same interval time of each day
    so that we split data set by date
    :param data_set:
    :return:
    '''
    date_list = count_data_set_date(data_set)
    data_sets = []
    for date in date_list:
        date_set = split_data_by_date(data_set,date)
        data_sets.append(date_set)
    return data_sets

def count_data_set_date(data_set):
    '''
    help method for how many date in our data.
    :param data_set:
    :return:
    '''
    ret = []
    for i in data_set:
        if i[0] not in ret:
            ret.append(i[0])
    return ret

def split_data_by_date(data_set,token):
    '''
    help method for cluster data from data set by given date(token)
    :param data_set:
    :param token:
    :return:
    '''
    token_list = []
    for i in data_set:
        if i[0] == token:
            token_list.append(i)
    return token_list


def divide_dataset(dataset):
    '''
    suppose our dataset have 4 attributes which are arrive time,
    start service time and end service time
    :param dataset:
    :return:
    '''
    arr_list,start_list,end_list = [],[],[]
    service_time_in_sec = []
    for i in dataset:
        date = i[0]
        t0 = convert_str_to_time(date+'-'+i[1])
        t1,t2 = convert_str_to_time(date+'-'+i[2]), convert_str_to_time(date+'-'+i[3])
        # service_time = (t2 - t1).seconds
        service_time = float((t2 - t1).seconds) / 60
        arr_list.append(t0)
        start_list.append(t1)
        end_list.append(t2)
        service_time_in_sec.append(service_time)


    return arr_list,start_list,end_list,service_time_in_sec

def convert_str_to_time(str_t):
    t = datetime.datetime.strptime(str_t, '%Y/%m/%d-%H:%M:%S')
    return t

def get_intrval_arrive_time(arr_list):
    arr_size = len(arr_list)
    int_arr = []
    for i in range(1,arr_size):
        t = float ( (arr_list[i] - arr_list[i -1]).seconds) / 60
        # t = (arr_list[i] - arr_list[i - 1]).seconds
        int_arr.append(t)

    return int_arr

def get_arr_service(data_set):
    '''
    for each data set split it into two sets
    i.e. inter arrival time list
    i.e. service time list
    :param data_set:
    :return:
    '''
    arr_list, start_list, end_list, service_time = divide_dataset(data_set)
    int_arr = get_intrval_arrive_time(arr_list)
    return int_arr, service_time

def make_total_sets(data_sets_dir):
    data_set = load_data(data_sets_dir)
    # abort first line "Date	Arrive	Start	Finish"
    splitted_sets = split_data_set(data_set)[1:]

    total_int_arr, total_service_time = [],[]
    for data_set in splitted_sets:
        int_arr, service_time = get_arr_service(data_set)
        total_int_arr += int_arr
        total_service_time += service_time
    list.sort(total_int_arr)
    list.sort(total_service_time)
    return total_int_arr,total_service_time

if __name__ ==  '__main__':
    data_dir = '/home/tian/PycharmProjects/312-Group/Final data.txt'
    total_int_arr, total_service_time = make_total_sets(data_dir)
    print len(total_int_arr), total_int_arr
    print len(total_service_time), total_service_time
