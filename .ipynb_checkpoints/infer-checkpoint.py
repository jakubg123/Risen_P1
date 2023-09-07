import os
from dataclasses import dataclass
import subprocess
import multiprocessing

@dataclass
class InferMetadata:
    speaker: str
    model_path: str
    config_path: str
    fm: str

def process_task(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        
        source, directory, object, data = item
        obj_path = os.path.join(source,directory,object) 
        part = object.split('_')
        saved = '_'.join(part[3:])
        for key in data.keys():
            if key in saved:
                out_path = os.path.join(target_dir, directory, object)
                command = f'svc infer -o {out_path} -s {data[key].speaker} -m {data[key].model_path} -c {data[key].config_path} -fm {data[key].fm} {obj_path}'
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                print(command)
                print(result.stdout)
                print(result.stderr)

if __name__ == "__main__":

    source_dir = "/home/jakubg/out"
    target_dir = "/home/jakubg/infered"





    fm = "crepe" 
    test = InferMetadata("speaker", "test_model_path", "test_config_path", "test_fm")
    
    g3_models = '/home/jakubg/maszyna_zipowanie/G_1215.pth'
    g3_config = '/home/jakubg/maszyna_zipowanie/configs/44k/config.json'
    
    actors_models = '/home/jakubg/svc/modele/M2/44k/G_609.pth'
    actors_config = '/home/jakubg/svc/modele/M2/44k/config.json'
    
    gothic_models = '/home/jakubg/logs/44k/G_311.pth'
    gothic_config = '/home/jakubg/logs/44k/config.json'

    data = {
    "PC_Hero": InferMetadata("Bezi_original",gothic_models,gothic_config,fm),
        
    "Weasel" : InferMetadata("Lester_original",gothic_models,gothic_config,fm),
    "Pavel" : InferMetadata("Fingers_original",gothic_models,gothic_config,fm),
    "Craig" : InferMetadata("Aleph_original",gothic_models,gothic_config,fm),
        
    "Doug" : InferMetadata("Milten_original",gothic_models,gothic_config,fm),
        
    "Belschwur" : InferMetadata("Gorn_original",gothic_models,gothic_config,fm),
    "Druid" : InferMetadata("Thorus_original",gothic_models,gothic_config,fm),
    "Eldric" : InferMetadata("Wilk_original",gothic_models,gothic_config,fm),

    "Abrax" : InferMetadata("CorAngar_original",gothic_models,gothic_config,fm), 
    "Domingo" : InferMetadata("Cronos_original",gothic_models,gothic_config,fm),
    "Hawkins" : InferMetadata("Lee_original",gothic_models,gothic_config,fm),

    "Sam" : InferMetadata("Diego_original",gothic_models,gothic_config,fm),
    "Cyrus" : InferMetadata("Gomez_original", gothic_models, gothic_config,fm),
    "Cole" : InferMetadata("Whistler_original", gothic_models, gothic_config, fm),
    "Walter" : InferMetadata("Mordrag_original", gothic_models, gothic_config, fm),
        
    "Inquisitor" : InferMetadata("Xardas_original",gothic_models,gothic_config,fm),
        
    "Santiago" : InferMetadata("YBerion_original",gothic_models,gothic_config,fm),
    "Felipe" : InferMetadata("Fisk_original",gothic_models,gothic_config,fm),
    "Sergio" : InferMetadata("Cipher_original",gothic_models,gothic_config,fm),

    
    "Don" : InferMetadata("audiobook15_bando",actors_models,actors_config,fm),
    "Ash" : InferMetadata("audiobook12_bobrowski",actors_models,actors_config,fm),
    "Leto" : InferMetadata("audiobook4_kosior",actors_models,actors_config,fm),
    "Luis" : InferMetadata("audiobook5_bajtlik",actors_models,actors_config,fm),
    "Brogar" : InferMetadata("audiobook6_jarocinski",actors_models,actors_config,fm),
    "Lorenzo" : InferMetadata("audiobook9_Lukomski",actors_models,actors_config,fm),
    "Delgado" : InferMetadata("audiobook14_grabowski",actors_models,actors_config,fm),
    "Fincher" : InferMetadata("audiobook11_zebrowski",actors_models,actors_config,fm),
    "Hernandez" : InferMetadata("audiobook13_corso",actors_models,actors_config,fm),
    "Carlos" : InferMetadata("audiobook8_defoe",actors_models,actors_config,fm),
    
    "Romanov" : InferMetadata("fraczewski",'/home/jakubg/svc/modele/fraczewski/G_4480.pth','/home/jakubg/svc/modele/fraczewski/config.json',fm), 
    "Pallas" : InferMetadata("ferdek",'/home/jakubg/svc/modele/ferdek/G_1600.pth','/home/jakubg/svc/modele/ferdek/config.json',fm), 
    "Danny" : InferMetadata("Knapik",'/home/jakubg/svc/modele/M1/GAJOS/G_2800.pth','/home/jakubg/svc/modele/M1/GAJOS/config.json',fm),
    
    "Enzo" : InferMetadata("Bufford",g3_models,g3_config,fm),
    "Taylor" : InferMetadata("Lee",g3_models,g3_config,fm),
        
    "Sabrosa" : InferMetadata("Zuben",g3_models,g3_config,fm),
        
    "Olf" : InferMetadata("Gonzales",g3_models,g3_config,fm),
    "Dytar" : InferMetadata("Basir",g3_models,g3_config,fm),

        
    "Ogre" : InferMetadata("Gorn_g3",g3_models,g3_config,fm),
    "Ukkos" : InferMetadata("Kan",g3_models,g3_config,fm),
    
        

    #Milten
    "Fuller" : InferMetadata("Rocko",g3_models,g3_config,"harvest"),
    "Lukor" : InferMetadata("Rufus",g3_models,g3_config, "parselmouth"),
    "Caspar" : InferMetadata("Peratur",g3_models,g3_config,fm),
    "Tristan" : InferMetadata("Murak",g3_models,g3_config,fm),

    "Esteban" : InferMetadata("KACZYNSKI",'/home/jakubg/svc/modele/kacz/G_5786.pth','/home/jakubg/svc/modele/kacz/config.json',fm)






}
    task_queue = multiprocessing.Queue()

    for directory in os.listdir(source_dir):
        os.makedirs(os.path.join(target_dir, directory), exist_ok=True)
        dir_path = os.path.join(source_dir, directory)
        for object in os.listdir(dir_path):
            obj_path = os.path.join(dir_path, object)
            if os.path.isfile(obj_path):
                if not os.path.exists(os.path.join(target_dir,directory,object)):
                    task_queue.put((source_dir, directory, object, data))
            else:
                pass
                os.makedirs(os.path.join(target_dir, directory, object), exist_ok=True)
                for file in os.listdir(obj_path):
                    file_path = os.path.join(obj_path, file)
                    out_pth = os.path.join(object,file)
                    if not os.path.exists(os.path.join(target_dir,directory,object,file)):
                        task_queue.put((source_dir, directory, out_pth, data))

    num_processes = 1 
    processes = []

    for _ in range(num_processes):
        process = multiprocessing.Process(target=process_task, args=(task_queue,))
        process.start()
        processes.append(process)

    for _ in range(num_processes):
        task_queue.put(None)

    for process in processes:
        process.join()

    print("All tasks have been processed.")
