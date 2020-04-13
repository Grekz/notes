from time import time, sleep
from get_args import get_args_predict
from time import time, sleep
from train_utils import get_transformers, get_datasets, get_dataloaders, get_model, get_criterion, get_optimizer, train
from helpers import get_device, load_checkpoint, load_names, predict

def main():
#   flowers/test/1/image_06743.jpg
#   checkpoints/cp_tmp.pth
    start_time = time()
    
    criterion = get_criterion()
    
    in_arg = get_args_predict()
    
    device = get_device(in_arg.gpu)
    
    model = load_checkpoint(in_arg.checkpoint_path, device)
    
    cat_to_name = load_names(in_arg.category_names)
    
    top_ps, top_class = predict(
        image_path=in_arg.image_path, 
        model=model, 
        cat_to_name=cat_to_name, 
        device=device,
        topk=in_arg.top_k
    )
    print(top_ps)
    print(top_class)
    
    tot_time = time() - start_time
    print(f"\n** Total Elapsed Runtime: {tot_time:.3f} seconds")
    
if __name__ == "__main__":
    main()
