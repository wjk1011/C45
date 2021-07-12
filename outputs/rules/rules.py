def findDecision(obj): #obj[0]: fixed acidity, obj[1]: volatile acidity, obj[2]: citric acid, obj[3]: residual sugar, obj[4]: chlorides, obj[5]: free sulfur dioxide, obj[6]: total sulfur dioxide, obj[7]: density, obj[8]: pH, obj[9]: sulphates, obj[10]: alcohol
	# {"feature": "volatile acidity", "instances": 1199, "metric_value": 0.9938, "depth": 1}
	if obj[1]<=1.0721729786396372:
		# {"feature": "alcohol", "instances": 1191, "metric_value": 0.9928, "depth": 2}
		if obj[10]<=11.508881360190847:
			# {"feature": "total sulfur dioxide", "instances": 1000, "metric_value": 0.9992, "depth": 3}
			if obj[6]<=112.36454511642876:
				# {"feature": "free sulfur dioxide", "instances": 942, "metric_value": 0.9998, "depth": 4}
				if obj[5]>1.0:
					# {"feature": "fixed acidity", "instances": 939, "metric_value": 0.9999, "depth": 5}
					if obj[0]>5.0:
						# {"feature": "citric acid", "instances": 937, "metric_value": 0.9998, "depth": 6}
						if obj[2]<=0.840015321689215:
							# {"feature": "sulphates", "instances": 936, "metric_value": 0.9998, "depth": 7}
							if obj[9]>0.39:
								# {"feature": "chlorides", "instances": 935, "metric_value": 0.9998, "depth": 8}
								if obj[4]>0.038:
									# {"feature": "density", "instances": 934, "metric_value": 0.9998, "depth": 9}
									if obj[7]>0.99236:
										# {"feature": "pH", "instances": 933, "metric_value": 0.9998, "depth": 10}
										if obj[8]>2.86:
											# {"feature": "residual sugar", "instances": 932, "metric_value": 0.9998, "depth": 11}
											if obj[3]>1.2:
												return 'good'
											elif obj[3]<=1.2:
												return 'bad'
											else: return 'bad'
										elif obj[8]<=2.86:
											return 'good'
										else: return 'good'
									elif obj[7]<=0.99236:
										return 'good'
									else: return 'good'
								elif obj[4]<=0.038:
									return 'good'
								else: return 'good'
							elif obj[9]<=0.39:
								return 'bad'
							else: return 'bad'
						elif obj[2]>0.840015321689215:
							return 'bad'
						else: return 'bad'
					elif obj[0]<=5.0:
						return 'bad'
					else: return 'bad'
				elif obj[5]<=1.0:
					return 'good'
				else: return 'good'
			elif obj[6]>112.36454511642876:
				# {"feature": "density", "instances": 58, "metric_value": 0.3621, "depth": 4}
				if obj[7]>0.9922:
					# {"feature": "pH", "instances": 57, "metric_value": 0.2975, "depth": 5}
					if obj[8]>2.93:
						# {"feature": "citric acid", "instances": 54, "metric_value": 0.133, "depth": 6}
						if obj[2]<=0.3075925925925926:
							# {"feature": "chlorides", "instances": 29, "metric_value": 0.2164, "depth": 7}
							if obj[4]>0.066:
								return 'bad'
							elif obj[4]<=0.066:
								# {"feature": "fixed acidity", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0]<=7.1:
									return 'bad'
								elif obj[0]>7.1:
									return 'good'
								else: return 'good'
							else: return 'bad'
						elif obj[2]>0.3075925925925926:
							return 'bad'
						else: return 'bad'
					elif obj[8]<=2.93:
						# {"feature": "citric acid", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=0.28:
							return 'good'
						elif obj[2]>0.28:
							return 'bad'
						else: return 'bad'
					else: return 'good'
				elif obj[7]<=0.9922:
					return 'good'
				else: return 'good'
			else: return 'bad'
		elif obj[10]>11.508881360190847:
			# {"feature": "citric acid", "instances": 191, "metric_value": 0.4673, "depth": 3}
			if obj[2]<=0.7485874620115041:
				# {"feature": "sulphates", "instances": 190, "metric_value": 0.4521, "depth": 4}
				if obj[9]>0.37:
					# {"feature": "pH", "instances": 189, "metric_value": 0.4363, "depth": 5}
					if obj[8]<=3.36037037037037:
						# {"feature": "residual sugar", "instances": 107, "metric_value": 0.134, "depth": 6}
						if obj[3]<=5.855023683543784:
							# {"feature": "fixed acidity", "instances": 98, "metric_value": 0.0821, "depth": 7}
							if obj[0]<=10.624435761113604:
								return 'good'
							elif obj[0]>10.624435761113604:
								# {"feature": "free sulfur dioxide", "instances": 13, "metric_value": 0.3912, "depth": 8}
								if obj[5]<=9.0:
									return 'good'
								elif obj[5]>9.0:
									# {"feature": "chlorides", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[4]>0.084:
										# {"feature": "density", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[7]>0.997:
											return 'good'
										elif obj[7]<=0.997:
											return 'bad'
										else: return 'bad'
									elif obj[4]<=0.084:
										return 'good'
									else: return 'good'
								else: return 'good'
							else: return 'good'
						elif obj[3]>5.855023683543784:
							# {"feature": "free sulfur dioxide", "instances": 9, "metric_value": 0.5033, "depth": 7}
							if obj[5]>3.0:
								return 'good'
							elif obj[5]<=3.0:
								return 'bad'
							else: return 'bad'
						else: return 'good'
					elif obj[8]>3.36037037037037:
						# {"feature": "fixed acidity", "instances": 82, "metric_value": 0.6864, "depth": 6}
						if obj[0]>5.363977221416096:
							# {"feature": "chlorides", "instances": 68, "metric_value": 0.7612, "depth": 7}
							if obj[4]<=0.09242912342642734:
								# {"feature": "free sulfur dioxide", "instances": 64, "metric_value": 0.7856, "depth": 8}
								if obj[5]>3.0:
									# {"feature": "residual sugar", "instances": 61, "metric_value": 0.8047, "depth": 9}
									if obj[3]>1.2:
										# {"feature": "density", "instances": 59, "metric_value": 0.8179, "depth": 10}
										if obj[7]<=0.9977577525155286:
											# {"feature": "total sulfur dioxide", "instances": 57, "metric_value": 0.8315, "depth": 11}
											if obj[6]>16.78574023276813:
												return 'good'
											elif obj[6]<=16.78574023276813:
												return 'bad'
											else: return 'bad'
										elif obj[7]>0.9977577525155286:
											return 'good'
										else: return 'good'
									elif obj[3]<=1.2:
										return 'good'
									else: return 'good'
								elif obj[5]<=3.0:
									return 'good'
								else: return 'good'
							elif obj[4]>0.09242912342642734:
								return 'good'
							else: return 'good'
						elif obj[0]<=5.363977221416096:
							return 'good'
						else: return 'good'
					else: return 'good'
				elif obj[9]<=0.37:
					return 'bad'
				else: return 'bad'
			elif obj[2]>0.7485874620115041:
				return 'bad'
			else: return 'bad'
		else: return 'good'
	elif obj[1]>1.0721729786396372:
		return 'bad'
	else: return 'bad'
