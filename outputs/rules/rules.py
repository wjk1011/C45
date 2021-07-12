def findDecision(obj): #obj[0]: fixed acidity, obj[1]: volatile acidity, obj[2]: citric acid, obj[3]: residual sugar, obj[4]: chlorides, obj[5]: free sulfur dioxide, obj[6]: total sulfur dioxide, obj[7]: density, obj[8]: pH, obj[9]: sulphates, obj[10]: alcohol
	# {"feature": "alcohol", "instances": 1199, "metric_value": 0.9972, "depth": 1}
	if obj[10]<=11.495106490443845:
		# {"feature": "chlorides", "instances": 983, "metric_value": 0.9927, "depth": 2}
		if obj[4]>0.038:
			# {"feature": "free sulfur dioxide", "instances": 981, "metric_value": 0.9923, "depth": 3}
			if obj[5]>1.0:
				# {"feature": "total sulfur dioxide", "instances": 979, "metric_value": 0.992, "depth": 4}
				if obj[6]<=112.76623800825877:
					# {"feature": "volatile acidity", "instances": 924, "metric_value": 0.9975, "depth": 5}
					if obj[1]<=1.0549127260018334:
						# {"feature": "density", "instances": 919, "metric_value": 0.9979, "depth": 6}
						if obj[7]>0.99236:
							# {"feature": "pH", "instances": 918, "metric_value": 0.9979, "depth": 7}
							if obj[8]>2.87:
								# {"feature": "residual sugar", "instances": 917, "metric_value": 0.9978, "depth": 8}
								if obj[3]>1.2:
									# {"feature": "fixed acidity", "instances": 915, "metric_value": 0.9979, "depth": 9}
									if obj[0]>5.0:
										# {"feature": "sulphates", "instances": 914, "metric_value": 0.998, "depth": 10}
										if obj[9]>0.33:
											# {"feature": "citric acid", "instances": 913, "metric_value": 0.9981, "depth": 11}
											if obj[2]<=0.44990739565595544:
												return 'bad'
											elif obj[2]>0.44990739565595544:
												return 'good'
											else: return 'good'
										elif obj[9]<=0.33:
											return 'bad'
										else: return 'bad'
									elif obj[0]<=5.0:
										return 'bad'
									else: return 'bad'
								elif obj[3]<=1.2:
									return 'bad'
								else: return 'bad'
							elif obj[8]<=2.87:
								return 'good'
							else: return 'good'
						elif obj[7]<=0.99236:
							return 'good'
						else: return 'good'
					elif obj[1]>1.0549127260018334:
						return 'bad'
					else: return 'bad'
				elif obj[6]>112.76623800825877:
					# {"feature": "residual sugar", "instances": 55, "metric_value": 0.3054, "depth": 5}
					if obj[3]<=9.580523821417628:
						# {"feature": "pH", "instances": 54, "metric_value": 0.2285, "depth": 6}
						if obj[8]>2.93:
							# {"feature": "volatile acidity", "instances": 52, "metric_value": 0.1371, "depth": 7}
							if obj[1]<=0.5932692307692308:
								# {"feature": "sulphates", "instances": 28, "metric_value": 0.2223, "depth": 8}
								if obj[9]>0.54:
									return 'bad'
								elif obj[9]<=0.54:
									# {"feature": "fixed acidity", "instances": 8, "metric_value": 0.5436, "depth": 9}
									if obj[0]<=7.9:
										return 'bad'
									elif obj[0]>7.9:
										# {"feature": "citric acid", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[2]>0.28:
											return 'bad'
										elif obj[2]<=0.28:
											return 'good'
										else: return 'good'
									else: return 'bad'
								else: return 'bad'
							elif obj[1]>0.5932692307692308:
								return 'bad'
							else: return 'bad'
						elif obj[8]<=2.93:
							# {"feature": "citric acid", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2]>0.28:
								return 'bad'
							elif obj[2]<=0.28:
								return 'good'
							else: return 'good'
						else: return 'good'
					elif obj[3]>9.580523821417628:
						return 'good'
					else: return 'good'
				else: return 'bad'
			elif obj[5]<=1.0:
				return 'good'
			else: return 'good'
		elif obj[4]<=0.038:
			return 'good'
		else: return 'good'
	elif obj[10]>11.495106490443845:
		# {"feature": "fixed acidity", "instances": 216, "metric_value": 0.4601, "depth": 2}
		if obj[0]>4.6:
			# {"feature": "citric acid", "instances": 215, "metric_value": 0.4465, "depth": 3}
			if obj[2]<=0.747983132328538:
				# {"feature": "sulphates", "instances": 214, "metric_value": 0.4324, "depth": 4}
				if obj[9]>0.37:
					# {"feature": "volatile acidity", "instances": 213, "metric_value": 0.4179, "depth": 5}
					if obj[1]<=0.9504600544443111:
						# {"feature": "residual sugar", "instances": 211, "metric_value": 0.4042, "depth": 6}
						if obj[3]<=7.200995442515706:
							# {"feature": "chlorides", "instances": 206, "metric_value": 0.3763, "depth": 7}
							if obj[4]>0.05074018838307268:
								# {"feature": "density", "instances": 181, "metric_value": 0.2852, "depth": 8}
								if obj[7]>0.9934542944558152:
									# {"feature": "pH", "instances": 159, "metric_value": 0.2318, "depth": 9}
									if obj[8]>3.172107308019395:
										# {"feature": "free sulfur dioxide", "instances": 135, "metric_value": 0.2623, "depth": 10}
										if obj[5]>4.446966755868139:
											# {"feature": "total sulfur dioxide", "instances": 122, "metric_value": 0.2829, "depth": 11}
											if obj[6]<=52.993686410713615:
												return 'good'
											elif obj[6]>52.993686410713615:
												return 'good'
											else: return 'good'
										elif obj[5]<=4.446966755868139:
											return 'good'
										else: return 'good'
									elif obj[8]<=3.172107308019395:
										return 'good'
									else: return 'good'
								elif obj[7]<=0.9934542944558152:
									# {"feature": "pH", "instances": 22, "metric_value": 0.5746, "depth": 9}
									if obj[8]<=3.39:
										return 'good'
									elif obj[8]>3.39:
										# {"feature": "total sulfur dioxide", "instances": 10, "metric_value": 0.8813, "depth": 10}
										if obj[6]>25.0:
											return 'good'
										elif obj[6]<=25.0:
											# {"feature": "free sulfur dioxide", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[5]<=11.0:
												return 'good'
											elif obj[5]>11.0:
												return 'bad'
											else: return 'bad'
										else: return 'bad'
									else: return 'good'
								else: return 'good'
							elif obj[4]<=0.05074018838307268:
								# {"feature": "density", "instances": 25, "metric_value": 0.795, "depth": 8}
								if obj[7]<=0.9955930867527552:
									# {"feature": "free sulfur dioxide", "instances": 24, "metric_value": 0.7383, "depth": 9}
									if obj[5]<=17.0:
										# {"feature": "total sulfur dioxide", "instances": 17, "metric_value": 0.874, "depth": 10}
										if obj[6]<=93.0:
											# {"feature": "pH", "instances": 15, "metric_value": 0.7219, "depth": 11}
											if obj[8]>3.39:
												return 'good'
											elif obj[8]<=3.39:
												return 'good'
											else: return 'good'
										elif obj[6]>93.0:
											return 'bad'
										else: return 'bad'
									elif obj[5]>17.0:
										return 'good'
									else: return 'good'
								elif obj[7]>0.9955930867527552:
									return 'bad'
								else: return 'bad'
							else: return 'good'
						elif obj[3]>7.200995442515706:
							# {"feature": "chlorides", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[4]<=0.051:
								return 'good'
							elif obj[4]>0.051:
								return 'bad'
							else: return 'bad'
						else: return 'good'
					elif obj[1]>0.9504600544443111:
						# {"feature": "residual sugar", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]<=1.6:
							return 'bad'
						elif obj[3]>1.6:
							return 'good'
						else: return 'good'
					else: return 'good'
				elif obj[9]<=0.37:
					return 'bad'
				else: return 'bad'
			elif obj[2]>0.747983132328538:
				return 'bad'
			else: return 'bad'
		elif obj[0]<=4.6:
			return 'bad'
		else: return 'bad'
	else: return 'good'
