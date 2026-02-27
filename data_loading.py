def load_data(path):
    df = pd.read_csv(path)
    print(f"Dataset shape: {df.shape}")
    return df

df = load_data(dataset_path)
