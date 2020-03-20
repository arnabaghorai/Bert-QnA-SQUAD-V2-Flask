

#subprocess.run('python Code/Test_Batch.py --paragraph Input_file.txt --model model/pytorch_model.bin --config_file Results/bert_config.json' ,  shell =

from Code.Inference import main

a = main(paragraph = "Enter para" , questions = ["Enter questions"])

print(a[0])
#print(a)
