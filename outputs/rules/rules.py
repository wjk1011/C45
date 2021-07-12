def findDecision(obj): #obj[0]: fixed acidity, obj[1]: volatile acidity, obj[2]: citric acid, obj[3]: residual sugar, obj[4]: chlorides, obj[5]: free sulfur dioxide, obj[6]: total sulfur dioxide, obj[7]: density, obj[8]: pH, obj[9]: sulphates, obj[10]: alcohol
	# {"feature": "alcohol", "instances": 1199, "metric_value": 0.9976, "depth": 1}
	if obj[10]<=11.473969415190453:
		# {"feature": "free sulfur dioxide", "instances": 993, "metric_value": 0.9934, "depth": 2}
		if obj[5]>1.0:
			# {"feature": "chlorides", "instances": 990, "metric_value": 0.9929, "depth": 3}
			if obj[4]>0.038:
				# {"feature": "total sulfur dioxide", "instances": 988, "metric_value": 0.9926, "depth": 4}
				if obj[6]<=113.62416081620776:
					# {"feature": "volatile acidity", "instances": 934, "metric_value": 0.9978, "depth": 5}
					if obj[1]<=1.0692622659554032:
						# {"feature": "density", "instances": 928, "metric_value": 0.9982, "depth": 6}
						if obj[7]>0.9929399999999999:
							# {"feature": "fixed acidity", "instances": 927, "metric_value": 0.9981, "depth": 7}
							if obj[0]>5.0:
								# {"feature": "citric acid", "instances": 926, "metric_value": 0.9982, "depth": 8}
								if obj[2]<=0.8411585237683546:
									# {"feature": "pH", "instances": 925, "metric_value": 0.9983, "depth": 9}
									if obj[8]>2.86:
										# {"feature": "sulphates", "instances": 924, "metric_value": 0.9982, "depth": 10}
										if obj[9]>0.33:
											# {"feature": "residual sugar", "instances": 923, "metric_value": 0.9983, "depth": 11}
											if obj[3]<=6.667481215774177:
												return 'bad'
											elif obj[3]>6.667481215774177:
												return 'good'
											else: return 'good'
										elif obj[9]<=0.33:
											return 'bad'
										else: return 'bad'
									elif obj[8]<=2.86:
										return 'good'
									else: return 'good'
								elif obj[2]>0.8411585237683546:
									return 'bad'
								else: return 'bad'
							elif obj[0]<=5.0:
								return 'bad'
							else: return 'bad'
						elif obj[7]<=0.9929399999999999:
							return 'good'
						else: return 'good'
					elif obj[1]>1.0692622659554032:
						return 'bad'
					else: return 'bad'
				elif obj[6]>113.62416081620776:
					# {"feature": "pH", "instances": 54, "metric_value": 0.3095, "depth": 5}
					if obj[8]>2.93:
						# {"feature": "residual sugar", "instances": 51, "metric_value": 0.1392, "depth": 6}
						if obj[3]<=6.9984980833118495:
							return 'bad'
						elif obj[3]>6.9984980833118495:
							# {"feature": "volatile acidity", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[1]>0.42:
								return 'bad'
							elif obj[1]<=0.42:
								return 'good'
							else: return 'good'
						else: return 'bad'
					elif obj[8]<=2.93:
						# {"feature": "citric acid", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=0.28:
							return 'good'
						elif obj[2]>0.28:
							return 'bad'
						else: return 'bad'
					else: return 'good'
				else: return 'bad'
			elif obj[4]<=0.038:
				return 'good'
			else: return 'good'
		elif obj[5]<=1.0:
			return 'good'
		else: return 'good'
	elif obj[10]>11.473969415190453:
		# {"feature": "fixed acidity", "instances": 206, "metric_value": 0.4751, "depth": 2}
		if obj[0]>4.6:
			# {"feature": "sulphates", "instances": 205, "metric_value": 0.4612, "depth": 3}
			if obj[9]>0.37:
				# {"feature": "residual sugar", "instances": 204, "metric_value": 0.4469, "depth": 4}
				if obj[3]<=7.06303114913308:
					# {"feature": "volatile acidity", "instances": 200, "metric_value": 0.4196, "depth": 5}
					if obj[1]<=0.997173839121868:
						# {"feature": "citric acid", "instances": 198, "metric_value": 0.405, "depth": 6}
						if obj[2]<=0.7030510268476787:
							# {"feature": "pH", "instances": 195, "metric_value": 0.3912, "depth": 7}
							if obj[8]<=3.3669743589743586:
								# {"feature": "chlorides", "instances": 107, "metric_value": 0.1845, "depth": 8}
								if obj[4]>0.05198611225552786:
									# {"feature": "density", "instances": 100, "metric_value": 0.1414, "depth": 9}
									if obj[7]<=0.9956362000000002:
										return 'good'
									elif obj[7]>0.9956362000000002:
										# {"feature": "total sulfur dioxide", "instances": 44, "metric_value": 0.2668, "depth": 10}
										if obj[6]<=25.59090909090909:
											# {"feature": "free sulfur dioxide", "instances": 29, "metric_value": 0.3621, "depth": 11}
											if obj[5]>4.0:
												return 'good'
											elif obj[5]<=4.0:
												return 'good'
											else: return 'good'
										elif obj[6]>25.59090909090909:
											return 'good'
										else: return 'good'
									else: return 'good'
								elif obj[4]<=0.05198611225552786:
									# {"feature": "free sulfur dioxide", "instances": 7, "metric_value": 0.5917, "depth": 9}
									if obj[5]>3.0:
										return 'good'
									elif obj[5]<=3.0:
										return 'bad'
									else: return 'bad'
								else: return 'good'
							elif obj[8]>3.3669743589743586:
								# {"feature": "density", "instances": 88, "metric_value": 0.5746, "depth": 8}
								if obj[7]>0.9922357543178619:
									# {"feature": "free sulfur dioxide", "instances": 73, "metric_value": 0.6447, "depth": 9}
									if obj[5]<=33.24779429141009:
										# {"feature": "total sulfur dioxide", "instances": 70, "metric_value": 0.661, "depth": 10}
										if obj[6]<=93.19766353556804:
											# {"feature": "chlorides", "instances": 65, "metric_value": 0.6194, "depth": 11}
											if obj[4]>0.039:
												return 'good'
											elif obj[4]<=0.039:
												return 'good'
											else: return 'good'
										elif obj[6]>93.19766353556804:
											# {"feature": "chlorides", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[4]<=0.049:
												return 'bad'
											elif obj[4]>0.049:
												return 'good'
											else: return 'good'
										else: return 'good'
									elif obj[5]>33.24779429141009:
										return 'good'
									else: return 'good'
								elif obj[7]<=0.9922357543178619:
									return 'good'
								else: return 'good'
							else: return 'good'
						elif obj[2]>0.7030510268476787:
							# {"feature": "chlorides", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[4]<=0.07400000000000001:
								return 'good'
							elif obj[4]>0.07400000000000001:
								return 'bad'
							else: return 'bad'
						else: return 'good'
					elif obj[1]>0.997173839121868:
						# {"feature": "citric acid", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]>0.24:
							return 'good'
						elif obj[2]<=0.24:
							return 'bad'
						else: return 'bad'
					else: return 'bad'
				elif obj[3]>7.06303114913308:
					# {"feature": "volatile acidity", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[1]<=0.3:
						return 'good'
					elif obj[1]>0.3:
						return 'bad'
					else: return 'bad'
				else: return 'bad'
			elif obj[9]<=0.37:
				return 'bad'
			else: return 'bad'
		elif obj[0]<=4.6:
			return 'bad'
		else: return 'bad'
	else: return 'good'
