import reproducibility_pkg as rp

if __name__ == '__main__':
    df = rp.gen_sample_data()
    is_reproducible = rp.try_reproducible_split(df)
    print("the random sample is reproducible:", is_reproducible)