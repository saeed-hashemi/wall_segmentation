import torch
from Models.models import SegmentationModule, build_encoder, build_decoder
def load(weights_encoder,weights_decoder):
    # Network Builders
    net_encoder = build_encoder(pretrained = False, train_only_wall = True)
    net_decoder = build_decoder(pretrained = False, train_only_wall = True)

    net_encoder.load_state_dict(  torch.load( weights_encoder, map_location = lambda storage, loc: storage ), strict = False )
    net_decoder.load_state_dict(  torch.load( weights_decoder, map_location = lambda storage, loc: storage ), strict = False )

    segmentation_module = SegmentationModule(net_encoder, net_decoder)
    segmentation_module.eval()
    # segmentation_module3.cuda()
    print('Models created!')
    return segmentation_module