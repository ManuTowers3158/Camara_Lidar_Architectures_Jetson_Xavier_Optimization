import argparse
from nuscenes.nuscenes import NuScenes


def validate_metadata(nusc):
    """
    Validates the consistency of metadata in a NuScenes dataset.
    Checks for missing 'prev' and 'next' token references in specific tables.

    Args:
        nusc (NuScenes): The NuScenes dataset object.
    """
    tables_to_validate = ['sample_data', 'sample_annotation', 'scene']
    missing_tokens = []

    for table in tables_to_validate:
        table_data = getattr(nusc, table)
        for record in table_data:
            for ref_field in ['prev', 'next']:
                if ref_field in record and record[ref_field]:
                    # Check if the token exists
                    try:
                        nusc.get(table, record[ref_field])
                    except KeyError:
                        missing_tokens.append((table, record['token'], ref_field, record[ref_field]))

    if missing_tokens:
        print("Missing tokens detected:")
        for table, token, ref_field, missing_token in missing_tokens:
            print(f"Table: {table}, Record Token: {token}, Missing Reference ({ref_field}): {missing_token}")
    else:
        print("All metadata references are valid.")


def main():
    """
    Main function to validate NuScenes metadata.
    """
    parser = argparse.ArgumentParser(description="Validate NuScenes metadata.")
    parser.add_argument(
        "--dataroot",
        type=str,
        required=True,
        help="Path to the NuScenes dataset root."
    )
    parser.add_argument(
        "--version",
        type=str,
        default="v1.0-mini",
        help="NuScenes dataset version (default: v1.0-mini)."
    )
    args = parser.parse_args()

    # Load the NuScenes dataset
    nusc = NuScenes(version=args.version, dataroot=args.dataroot, verbose=True)

    # Validate metadata
    validate_metadata(nusc)


if __name__ == "__main__":
    main()
