import pandas as pd
import numpy as np
import plotly.express as px


def read_data(file_path):
    """
    Reads data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    DataFrame: Pandas DataFrame containing the data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: File is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: File could not be parsed.")
        return None


def process_data(data):
    """
    Processes the data to calculate total and defective chips and their percentages.

    Parameters:
    data (DataFrame): The input data.

    Returns:
    DataFrame: Processed data with total and defective chip counts and percentages.
    """
    grouped_data = (
        data.groupby("date")
        .agg({"produced_chips": "sum", "defective_chips": "sum"})
        .reset_index()
    )
    grouped_data["defective_percentage"] = (
        grouped_data["defective_chips"] / grouped_data["produced_chips"]
    ) * 100
    grouped_data["defective_percentage"] = grouped_data["defective_percentage"].round(2)
    return grouped_data


def visualize_data(grouped_data):
    """
    Visualizes the processed data with line graphs.

    Parameters:
    grouped_data (DataFrame): The processed data.
    """
    fig = px.line(
        grouped_data,
        x="date",
        y=["produced_chips", "defective_percentage"],
        labels={
            "value": "Количество / Процент",
            "date": "Дата",
            "variable": "Променлива",
        },
        title="Произведени чипове и процент на дефектни чипове по дати",
    )
    fig.show()


def save_processed_data(grouped_data, file_path):
    """
    Saves the processed data to a new CSV file.

    Parameters:
    grouped_data (DataFrame): The processed data.
    file_path (str): The path to the output CSV file.
    """
    grouped_data.to_csv(file_path, index=False)


def calculate_statistics(grouped_data):
    """
    Calculates statistical metrics from the processed data.

    Parameters:
    grouped_data (DataFrame): The processed data.

    Returns:
    tuple: Mean and standard deviation of produced chips.
    """
    mean_produced_chips = np.mean(grouped_data["produced_chips"])
    std_produced_chips = np.std(grouped_data["produced_chips"])
    return mean_produced_chips, std_produced_chips


def analyze_defective_percentage(grouped_data):
    """
    Analyzes and prints dates with high defective chip percentages.

    Parameters:
    grouped_data (DataFrame): The processed data.
    """
    for index, row in grouped_data.iterrows():
        if row["defective_percentage"] > 5:
            print(
                f"Внимание: Висок процент дефектни чипове на дата {row['date']}: {row['defective_percentage']:.2f}%"
            )


def additional_analysis(data):
    """
    Performs additional analysis on wafer size, shifts, and machines.

    Parameters:
    data (DataFrame): The input data.
    """
    # Analysis by wafer size
    average_defect_rate_by_wafer_size = (
        data.groupby("wafer_size")["defective_chips"].sum()
        / data.groupby("wafer_size")["produced_chips"].sum()
        * 100
    ).round(2)
    print(
        f"\n Среден процент дефектни чипове по размер на пластината: {average_defect_rate_by_wafer_size}"
    )

    # Analysis by shift
    average_defect_rate_by_shift = (
        data.groupby("shift")["defective_chips"].sum()
        / data.groupby("shift")["produced_chips"].sum()
        * 100
    ).round(2)
    print(f"\n Среден процент дефектни чипове по смяна: {average_defect_rate_by_shift}")

    # Analysis by machine
    average_defect_rate_by_machine = (
        data.groupby("machine_id")["defective_chips"].sum()
        / data.groupby("machine_id")["produced_chips"].sum()
        * 100
    ).round(2)
    print(
        f"\n Среден процент дефектни чипове по машина: {average_defect_rate_by_machine}"
    )

    # Visualization of the additional analyses
    fig_wafer_size = px.bar(
        average_defect_rate_by_wafer_size,
        labels={"value": "Среден процент (%)", "wafer_size": "Размер на пластината"},
        title="Среден процент (%) дефектни чипове по размер на пластината",
    )
    fig_wafer_size.show()

    fig_shift = px.bar(
        average_defect_rate_by_shift,
        labels={"value": "Среден процент (%)", "shift": "Смяна"},
        title="Среден процент (%) дефектни чипове по смяна",
    )
    fig_shift.show()

    fig_machine = px.bar(
        average_defect_rate_by_machine,
        labels={
            "value": "Среден процент (%)",
            "machine_id": "Идентификатор на машината",
        },
        title="Среден процент (%) дефектни чипове по машина",
    )
    fig_machine.show()


# Main script execution
if __name__ == "__main__":
    data = read_data("semiconductor_production.csv")
    if data is not None:
        grouped_data = process_data(data)
        visualize_data(grouped_data)
        save_processed_data(grouped_data, "processed_semiconductor_production.csv")

        mean_produced_chips, std_produced_chips = calculate_statistics(grouped_data)
        print(f"\n Средно произведени чипове: {mean_produced_chips:.2f}")
        print(
            f"Стандартно отклонение на произведените чипове: {std_produced_chips:.2f}"
        )

        analyze_defective_percentage(grouped_data)
        additional_analysis(data)
