
# Monthly Distribution Yield Calculator

This Python script calculates the monthly distribution yield of an investment after accounting for management fees. It provides the total adjusted monthly distribution income, the monthly distribution yield percentage, and the monthly management fee.

## Features

- **Total Monthly Distribution Income**: Calculates the total distribution income after deducting management fees.
- **Monthly Distribution Yield**: Computes the yield percentage based on the adjusted monthly distribution and the initial investment.
- **Management Fees Calculation**: Accounts for the management fees as a percentage of the initial investment.

## Requirements

- Python 3.x

## Usage

1. **Define Parameters**: Set the following parameters in the script:
    - `distribution_per_share`: The distribution per share in dollars.
    - `share_price`: The share price in dollars.
    - `num_shares_owned`: The number of shares owned.
    - `management_fee_percentage`: The management fee percentage.

2. **Run the Script**: Execute the script to calculate and print the results.

### Example

```python
# Example usage
distribution_per_share = 0.55  # Example distribution per share in dollars
share_price = 45           # Example share price in dollars
num_shares_owned = 590       # Example number of shares owned
management_fee_percentage = 0.4  # Management fee percentage

adjusted_distribution, monthly_yield, management_fee = calculate_monthly_distribution_yield(
    distribution_per_share, share_price, num_shares_owned, management_fee_percentage)

print(f"Total Monthly Distribution Income (after management fees): ${adjusted_distribution:.2f}")
print(f"Monthly Distribution Yield: {monthly_yield:.2f}%")
print(f"Monthly Management Fee: ${management_fee:.2f}")
```

## Functions

### `calculate_monthly_distribution_yield(distribution_per_share, share_price, num_shares_owned, management_fee_percentage)`

Calculates the monthly distribution yield and returns the adjusted monthly distribution income, monthly distribution yield, and management fee.

- **Parameters**:
  - `distribution_per_share` (float): Distribution per share in dollars.
  - `share_price` (float): Share price in dollars.
  - `num_shares_owned` (int): Number of shares owned.
  - `management_fee_percentage` (float): Management fee percentage.

- **Returns**:
  - `adjusted_monthly_distribution` (float): Adjusted monthly distribution income after management fees.
  - `monthly_distribution_yield` (float): Monthly distribution yield percentage.
  - `management_fee` (float): Monthly management fee in dollars.

## License

This project is licensed under the MIT License.
