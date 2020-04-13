
from time import time, sleep
from get_args import get_args_train
from train_utils import get_transformers, get_datasets, get_dataloaders, get_model, get_criterion, get_optimizer, train
from helpers import get_device, save_checkpoint


def main():
    start_time = time()

    in_arg = get_args_train()

    data_dir = in_arg.data_dir

    device = get_device(in_arg.gpu)
#     print(device)
    dataloaders = get_dataloaders(data_dir)

    criterion = get_criterion()

    model = get_model(
        device=device,
        arch=in_arg.arch,
        hidden_units=in_arg.hidden_units,
        data_dir=in_arg.data_dir,
        save_dir=in_arg.save_dir
    )
    # print(model)

    optimizer = get_optimizer(model, in_arg.learning_rate)
#     print(optimizer)

    train(
        model,
        criterion,
        optimizer,
        epochs=in_arg.epochs,
        device=device,
        train_loader=dataloaders['train'],
        valid_loader=dataloaders['valid']
    )

    tot_time = time() - start_time
    print(f"\n** Total Elapsed Runtime: {tot_time:.3f} seconds")


if __name__ == "__main__":
    main()
