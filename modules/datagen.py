import numpy as np
from PIL import Image
import random
import os
import itertools
from tqdm import tqdm

# @jit
def get_triplets(ids,BASE_PATH):
    triplets=[]
    for id_ in ids:
        files = sorted([BASE_PATH+id_+'/'+x for x in os.listdir(BASE_PATH+id_)])
        con = sorted([x for x in files if 'comsumer' in x])
        shop = sorted([x for x in files if 'shop' in x ])
        combs = list(itertools.product(tuple(con),tuple(shop)))
        for comb in combs:
            comb = list(comb)
            neg_id = random.choice([x for x in ids if x != id_])
            neg_file = random.choice([BASE_PATH+neg_id+'/'+x for x in os.listdir(BASE_PATH+neg_id) if 'shop' in x])
            comb.append(neg_file)
            triplets.append(comb)
    return triplets

# @jit
def get_np_triplets(triplet_PATHs):
    triplets = []
    # triplets = np.ndarray
    for triplet in tqdm(triplet_PATHs):

#         anc_img = Image.fromarray(np.uint8(triplet[0])).convert('RGB')
#         pos_img = Image.fromarray(np.uint8(triplet[1])).convert('RGB')
#         neg_img = Image.fromarray(np.uint8(triplet[2])).convert('RGB')

        anc_img = Image.open(triplet[0]).convert('RGB')
        pos_img = Image.open(triplet[1]).convert('RGB')
        neg_img = Image.open(triplet[2]).convert('RGB')

        anc_img = np.array(anc_img.resize((128,128)))/255. #resize to (128,128,3)
        pos_img = np.array(pos_img.resize((128,128)))/255.    
        neg_img = np.array(neg_img.resize((128,128)))/255.    

        tri = [anc_img,pos_img,neg_img]
        triplets.append(np.array(tri))

    triplets = np.array(triplets)
    return triplets

def get_test_pairs(test_ids,BASE_PATH,seed_num):
    # test_pairのリスト
    test_pairs=[]
    # idの選択の仕方をランダムにしたらいいのか？
    for id_ in tqdm(test_ids):
        # test pair = [product_id,[query_img_path,ans_img_path]]
        test_pair = []
        test_pair.append(int(id_[3:]))
        files = sorted([BASE_PATH+id_+'/'+x for x in os.listdir(BASE_PATH+id_)])
        con = sorted([x for x in files if 'comsumer' in x])
        shop = sorted([x for x in files if 'shop' in x ])
        combs = list(itertools.product(tuple(con),tuple(shop)))
#         print(combs)
        np.random.seed(seed=seed_num)
        # choice one pair from combs
        test_pair.append(list(combs[np.random.randint(len(combs))]))
        test_pairs.append(test_pair)
    return test_pairs
    
    
    
    
    
    
    
    
    
    
    
    