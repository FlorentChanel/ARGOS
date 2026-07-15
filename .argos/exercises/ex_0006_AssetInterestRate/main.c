// Author: HE-Arc

// Standard includes
#include <stdio.h>

// Local includes
#include "ex_0006_AssetInterestRate.h"

int main(void)
{
  double initAssets = 0.0;
  double interestRate = 0.0;
  double duration = 0.0;
  double finalAssets = 0.0;

  printf("What is your initial asset? ");
  scanf("%lf", &initAssets);

  printf("What is your yearly interest rate (in percent)? ");
  scanf("%lf", &interestRate);

  printf("Duration in years? ");
  scanf("%lf", &duration);

  finalAssets = ex_0006_AssetInterestRate(initAssets, interestRate, duration);

  printf("\nAfter %.0f years, your assets (with interest) will be %10.2f SFr\n\n", duration, finalAssets);

  return 0;
}
