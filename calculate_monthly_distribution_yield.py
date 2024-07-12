def calculate_monthly_distribution_yield(distribution_per_share, share_price, num_shares_owned, management_fee_percentage):
    # Calculate the total monthly distribution income
    total_monthly_distribution = distribution_per_share * num_shares_owned
    
    # Calculate the initial investment based on the share price and number of shares owned
    initial_investment = share_price * num_shares_owned
    
    # Calculate the management fees
    management_fee = (management_fee_percentage / 100) * initial_investment / 12
    
    # Adjust the total monthly distribution by subtracting the management fees
    adjusted_monthly_distribution = total_monthly_distribution - management_fee
    
    # Calculate the monthly distribution yield as a percentage
    monthly_distribution_yield = (adjusted_monthly_distribution / initial_investment) * 100
    
    return adjusted_monthly_distribution, monthly_distribution_yield, management_fee

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
