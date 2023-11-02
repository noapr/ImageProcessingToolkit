import torch
import torchvision
import torchvision.transforms as transforms


def load_cifar10():
    transform = transforms.Compose([transforms.ToTensor(), ])
    train_set = torchvision.datasets.CIFAR10(root='../dataset', train=True, download=True, transform=transform)
    test_set = torchvision.datasets.CIFAR10(root='../dataset', train=False, download=True, transform=transform)
    train_loader = torch.utils.data.DataLoader(train_set, batch_size=4, shuffle=True, num_workers=2)
    test_loader = torch.utils.data.DataLoader(test_set, batch_size=4, shuffle=False, num_workers=2)
    return train_loader, test_loader


def create_bw_color_pairs():
    train_loader, _ = load_cifar10()

    for i, (color_image, label) in enumerate(train_loader, 0):
        grayscale_image = torch.mean(color_image, dim=1, keepdim=True)
        torchvision.utils.save_image(grayscale_image, f'../dataset/bw_images/bw_image_{i}.png')
        torchvision.utils.save_image(color_image, f'../dataset/color_images/color_image_{i}.png')


if __name__ == '__main__':
    create_bw_color_pairs()
