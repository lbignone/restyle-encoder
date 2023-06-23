dataset_paths = {
	'ffhq': '',
	'celeba_test': '',

	'cars_train': '',
	'cars_test': '',

	'church_train': '',
	'church_test': '',

	'horse_train': '',
	'horse_test': '',

	'afhq_wild_train': '',
	'afhq_wild_test': '',
    
	'eagle_train': '/home/lbignone/Development/stylegan3-editing/data/eagle_galrand_64x64/train',
	'eagle_test': '/home/lbignone/Development/stylegan3-editing/data/eagle_galrand_64x64/test',
    
	'eagle_galface_256x256_train': '/home/lbignone/Development/stylegan3-editing/data/eagle_galface_256x256/train',
	'eagle_galface_256x256_test': '/home/lbignone/Development/stylegan3-editing/data/eagle_galface_256x256/test',
}

model_paths = {
	'ir_se50': 'pretrained_models/model_ir_se50.pth',
	'resnet34': 'pretrained_models/resnet34-333f7ec4.pth',
	'stylegan_ffhq': 'pretrained_models/stylegan2-ffhq-config-f.pt',
	'stylegan_cars': 'pretrained_models/stylegan2-car-config-f.pt',
	'stylegan_church': 'pretrained_models/stylegan2-church-config-f.pt',
	'stylegan_horse': 'pretrained_models/stylegan2-horse-config-f.pt',
	'stylegan_ada_wild': 'pretrained_models/afhqwild.pt',
	'stylegan_toonify': 'pretrained_models/ffhq_cartoon_blended.pt',
	'shape_predictor': 'pretrained_models/shape_predictor_68_face_landmarks.dat',
	'circular_face': 'pretrained_models/CurricularFace_Backbone.pth',
	'mtcnn_pnet': 'pretrained_models/mtcnn/pnet.npy',
	'mtcnn_rnet': 'pretrained_models/mtcnn/rnet.npy',
	'mtcnn_onet': 'pretrained_models/mtcnn/onet.npy',
	'moco': 'pretrained_models/moco_v2_800ep_pretrain.pt'
}
