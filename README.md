[![INFORMS Journal on Computing Logo](https://INFORMSJoC.github.io/logos/INFORMS_Journal_on_Computing_Header.jpg)](https://pubsonline.informs.org/journal/ijoc)

# Deterring the Gray Market: Product Diversion Detection via Learning Disentangled Representations of Multivariate Time Series

This archive is distributed in association with the [INFORMS Journal on
Computing](https://pubsonline.informs.org/journal/ijoc) under the [MIT License](LICENSE).

The software and data in this repository are a snapshot of the software and data
that were used in the research reported on in the paper 
[Deterring the Gray Market: Product Diversion Detection via Learning Disentangled Representations of Multivariate Time Series](https://doi.org/10.1287/ijoc.2022.0155) by Hao Lin, Guannan Liu, Junjie Wu, and J. Leon Zhao.

## Cite

To cite the contents of this repository, please cite both the paper and this repo, using their respective DOIs.

https://doi.org/10.1287/ijoc.2022.0155

https://doi.org/10.1287/ijoc.2022.0155.cd

Below is the BibTex for citing this snapshot of the respoitory.

```
@article{lin2023deterring,
  author =        {Lin, Hao and Liu, Guannan and Wu, Junjie and Zhao, J Leon},
  publisher =     {INFORMS Journal on Computing},
  title =         {Deterring the Gray Market: Product Diversion Detection via Learning Disentangled Representations of Multivariate Time Series},
  year =          {2023},
  doi =           {10.1287/ijoc.2022.0155.cd},
  url =           {https://github.com/INFORMSJoC/2022.0155},
}  
```

## Contact Details

If you have questions about the paper or the code, please contact Dr. Hao Lin [haolin@buaa.edu.cn](mailto:haolin@buaa.edu.cn).

## Description

The goal of this software is to facilitate readers to reproduce the experimental results in this paper. The experiments verify the effectiveness of the proposed model on both real-world and synthetic data sets.

## Environment Requirements

To run the code, you will need to make sure that you have the following dependencies installed:

* `Python` 3.6 with `pytorch` 1.4.0, `numpy`, `scikit-learn`, `matplotlib`

## Replicating

1. Please firstly download and prepare the data sets according to the instructions in [data/README.md](data/README.md).

2. To replicate the results of our proposed model in [Table 1](results/table1.png) of the paper, please do the following commands:
```
cd scripts
python run_empirical_data_set.py
```
The script is to conduct 10 independent runs to obtain the average AUROC with standard deviations and the average AUPRC with standard deviations. It is expected to be completed in roughly one hour with a maximum cost of 8 GB memory if ran with CPUs on a Linux Server. The script will output the following results and will also generate a log file that can be found in [results/result_dataset_hp.txt](results/result_dataset_hp.txt).
```
Number of runs:  10 , Mean of AUROC:  0.9509500000000001 , STD of AUROC:  0.01018422800216098
Number of runs:  10 , Mean of AUPRC:  0.31303 , STD of AUPRC:  0.07672194014752233
```
Note: the results may show some stochasticity due to the random parameter initialization process of neural networks.

## Results

![image](results/table1.png)

## Acknowledgement

We would like to thank the editors and anonymous reviewers for their detailed and constructive feedbacks in helping improve the paper.

## Ongoing Development

This code is being developed on an on-going basis at the author's
[Github site](https://github.com/linhaobuaa/IJOC.2022.0155).

## Support

For support in using this software, please submit an
[issue](https://github.com/linhaobuaa/IJOC.2022.0155/issues/new).
