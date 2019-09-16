import os


def process(input, loops, output, weight1, weight2 ):
    #调用foliation-cli.exe
    exepath = "foliation-cli.exe -m {} -l {} -o {} --weights {} {} --verbose"\
        .format(input, loops, output, weight1, weight2)
    os.system(exepath)


def text_save(content,filename,mode='w'):
    # 保存列表到txt
    file = open(filename,mode)
    for i in range(len(content)):
        file.write(str(content[i])+'\n')
    file.close()


def text_read(filename):
    # 从txt读取列表
    try:
        file = open(filename,'r')
    except IOError:
        error = []
        return error
    content = file.readlines()

    for i in range(len(content)):
        content[i] = content[i][:len(content[i])-1]

    file.close()
    return content
def list_str(list):
    # 将列表变为字符串
    Str = str()
    for i in list:
        Str += str(i)
    
    return Str



def main(weights):
    #主程序
    weights_str = list_str(weights)

    recorder_path = "finished_loops.txt"
    finished_loops = text_read(recorder_path)

    main_path = os.path.dirname(os.path.split(os.path.abspath(__file__))[0])
    model_path = main_path +'\\testmodel\\'
    for model_files in os.listdir(model_path): ##遍历testmodel文件夹
        model_file = model_path + model_files
        if os.path.isdir(model_file):
            for models in os.listdir(model_file): ##遍历testmodel下文件夹文件
                model = model_file + "\\" + models
                if os.path.isdir(model):
                    for off in os.listdir(model):
                        if off.endswith(".off"):
                            imput_path = model + "\\" + off
                            off_name = off.split(".")[0].split("_")
                            off_len = len(off_name)
                            for loops in os.listdir(model):
                                if loops not in finished_loops:
                                    if loops.endswith(".loops"):
                                        if loops.split("_")[:off_len] == off_name :
                                            loops_path = model + "\\" + loops
                                            result_name = loops.split(".")[0] +"_"+ weights_str + ".om"
                                            output_path = model_path + "results\\" + models + "\\" + result_name
                                            process(imput_path, loops_path, output_path, weights[0], weights[1])
                                            finished_loops.append(loops)
                                            text_save(finished_loops, recorder_path)
                                            print(imput_path, "\n",
                                                  loops_path, "\n",
                                                  output_path)

    

if __name__ == "__main__":
    os.chdir(os.getcwd())
    weights = [1, 1, 1, 1, 1, 1, 1, 1]
    main(weights)