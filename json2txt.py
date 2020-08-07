import json
import os
database_name = "people"

txt_file = open('data/'+database_name+'/'+'Result/'+database_name+'.txt','w')
all_data_string=""
with open("data/people/Result/people.json", "r") as data_file:
    single_frame_string=""
    data_dict = json.load(data_file)
    for single_frame_data in data_dict['calibInfo']['VideoChannels'][0]['VideoInfo']['mapFrameInfos']:
        single_frame_string+=single_frame_data['key']['FrameNum']+" "+str(len(single_frame_data['value']['mapTargets']))+" "
        # print(single_frame_data['key']['FrameNum'])
        # print(len(single_frame_data['value']['mapTargets']))
        for single_target_data in single_frame_data['value']['mapTargets']:
            # single_target_data['value']['Vertex'][0]['fX'] = left
            # single_target_data['value']['Vertex'][0]['fY'] = top
            # single_target_data['value']['Vertex'][1]['fX'] = right
            # single_target_data['value']['Vertex'][1]['fY'] = top
            # single_target_data['value']['Vertex'][2]['fX'] = right
            # single_target_data['value']['Vertex'][2]['fY'] = bottom
            # single_target_data['value']['Vertex'][3]['fX'] = left
            # single_target_data['value']['Vertex'][3]['fY'] = bottom
            single_target_coordinate_list = [single_target_data['value']['Vertex'][0]['fX'],single_target_data['value']['Vertex'][0]['fY'],single_target_data['value']['Vertex'][1]['fX'],single_target_data['value']['Vertex'][2]['fY']]
            for coordinate in single_target_coordinate_list:
                single_frame_string += str(coordinate)+" "
            single_frame_string +=str(single_target_data['value']['TargetType'])+" "
            # print(single_target_coordinate_list)
            # print(single_target_data['value']['TargetType'])
            #注意输入的bbox信息格式应该是两点式，即左上角点xy坐标和右下角点xy坐标(x1,y1,x2,y2)
        single_frame_string+="\n"
    print(single_frame_string)
all_data_string+=single_frame_string
txt_file.write(all_data_string)
txt_file.close()