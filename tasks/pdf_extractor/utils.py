import pandas as pd

# Dataframe Generator

def generate_dataframe(original_df: pd.DataFrame, chunks: list, inference_parameters: dict):
    '''
    Generate an output dataframe containing the chunk filed and replicate original data
    
    Params:
        original_df: pd.DataFrame
        chunks: List
        inference_parameters: dict
    '''
    
    # Chunk column
    output_column_name = inference_parameters['output_column_name']
    
    # Initializate new dataframe
    output_df_columns = list(original_df.columns) + [output_column_name]
    output_df = pd.DataFrame(columns = output_df_columns)
    
    # Iterate over each row of original dataframe
    for chunk_idx, row in original_df.iterrows():

        # Get chunks
        row_chunks = chunks[chunk_idx]
        num_chunks = len(row_chunks)

        # Replicate other df columns based on the num of chunks
        row_columns = row.keys()
        replicated_data = {}
        for row_column in row_columns:
            replicated_data[row_column] = [row[row_column]]*num_chunks
        
        # Add chunks
        replicated_data[output_column_name] = row_chunks

        # Row dataframe
        row_df = pd.DataFrame(replicated_data)

        # Add to new dataframe
        output_df = pd.concat((output_df, row_df))
    
    output_df = output_df.reset_index(drop=True)
    
    return output_df