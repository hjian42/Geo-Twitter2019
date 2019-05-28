# Logs

### May 27

1. finalized data for USA and UK
	- run `preprocess_tokenize.py`, then run `prepare_data_adagram.py` to get:
		- `{country}_tokenized.txt` and `{country}_tok_pos.txt` for USA and UK
		- `usa_uk.txt` and `usa_uk.dict`
2. train AdaGram using `usa_uk.txt` on EC2 (adagram)

```
export PATH="/home/ec2-user/julia-ae26b25d43/bin:$PATH"
cd ~/.julia/v0.4/AdaGram/

# trial for dialects_04.model
sh train.sh --min-freq 20 --window 10 --workers 4 --dim 300 --prototypes 30 --alpha 0.1 --epochs 3 --sense-treshold 1e-17 ~/dialects3_tokenized.txt  ~/dialects3.dict ./dialects.model

# trial 1:
sh train.sh --min-freq 20 --window 10 --workers 4 --dim 100 --prototypes 30 --alpha 0.1 --epochs 1 --sense-treshold 1e-17 ~/usa_uk.txt  ~/usa_uk.dict ./usa_uk_05_27_trial1.model

```


