def findDecision(obj): #obj[0]: fixed acidity, obj[1]: volatile acidity, obj[2]: citric acid, obj[3]: residual sugar, obj[4]: chlorides, obj[5]: free sulfur dioxide, obj[6]: total sulfur dioxide, obj[7]: density, obj[8]: pH, obj[9]: sulphates, obj[10]: alcohol
	# {"feature": "alcohol", "instances": 1199, "metric_value": 0.9992, "depth": 1}
	if obj[10]<=11.471743979595093:
		# {"feature": "chlorides", "instances": 1001, "metric_value": 0.9898, "depth": 2}
		if obj[4]>0.038:
			# {"feature": "free sulfur dioxide", "instances": 999, "metric_value": 0.9894, "depth": 3}
			if obj[5]>1.0:
				# {"feature": "density", "instances": 997, "metric_value": 0.989, "depth": 4}
				if obj[7]>0.99236:
					# {"feature": "pH", "instances": 996, "metric_value": 0.9888, "depth": 5}
					if obj[8]>2.86:
						# {"feature": "volatile acidity", "instances": 995, "metric_value": 0.9886, "depth": 6}
						if obj[1]<=1.0807672465622635:
							# {"feature": "total sulfur dioxide", "instances": 988, "metric_value": 0.9897, "depth": 7}
							if obj[6]<=115.19909680309331:
								# {"feature": "fixed acidity", "instances": 931, "metric_value": 0.996, "depth": 8}
								if obj[0]>5.2:
									# {"feature": "sulphates", "instances": 930, "metric_value": 0.9961, "depth": 9}
									if obj[9]>0.33:
										# {"feature": "citric acid", "instances": 929, "metric_value": 0.9962, "depth": 10}
										if obj[2]<=0.256264800861141:
											# {"feature": "residual sugar", "instances": 502, "metric_value": 0.9712, "depth": 11}
											if obj[3]<=5.675907875476762:
												return 'bad'
											elif obj[3]>5.675907875476762:
												return 'good'
											else: return 'good'
										elif obj[2]>0.256264800861141:
											# {"feature": "residual sugar", "instances": 427, "metric_value": 0.9957, "depth": 11}
											if obj[3]>1.3:
												return 'good'
											elif obj[3]<=1.3:
												return 'bad'
											else: return 'bad'
										else: return 'good'
									elif obj[9]<=0.33:
										return 'bad'
									else: return 'bad'
								elif obj[0]<=5.2:
									return 'bad'
								else: return 'bad'
							elif obj[6]>115.19909680309331:
								# {"feature": "residual sugar", "instances": 57, "metric_value": 0.3666, "depth": 8}
								if obj[3]<=7.941735903697198:
									# {"feature": "sulphates", "instances": 55, "metric_value": 0.2254, "depth": 9}
									if obj[9]<=1.8442300228724333:
										return 'bad'
									elif obj[9]>1.8442300228724333:
										# {"feature": "citric acid", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[2]<=0.28:
											return 'good'
										elif obj[2]>0.28:
											return 'bad'
										else: return 'bad'
									else: return 'good'
								elif obj[3]>7.941735903697198:
									return 'good'
								else: return 'good'
							else: return 'bad'
						elif obj[1]>1.0807672465622635:
							return 'bad'
						else: return 'bad'
					elif obj[8]<=2.86:
						return 'good'
					else: return 'good'
				elif obj[7]<=0.99236:
					return 'good'
				else: return 'good'
			elif obj[5]<=1.0:
				return 'good'
			else: return 'good'
		elif obj[4]<=0.038:
			return 'good'
		else: return 'good'
	elif obj[10]>11.471743979595093:
		# {"feature": "fixed acidity", "instances": 198, "metric_value": 0.4561, "depth": 2}
		if obj[0]<=13.920456847074043:
			# {"feature": "citric acid", "instances": 197, "metric_value": 0.441, "depth": 3}
			if obj[2]<=0.7379684184330622:
				# {"feature": "sulphates", "instances": 196, "metric_value": 0.4255, "depth": 4}
				if obj[9]>0.37:
					# {"feature": "volatile acidity", "instances": 195, "metric_value": 0.4094, "depth": 5}
					if obj[1]<=0.987688211146936:
						# {"feature": "residual sugar", "instances": 193, "metric_value": 0.3941, "depth": 6}
						if obj[3]<=7.040785216351962:
							# {"feature": "pH", "instances": 190, "metric_value": 0.3795, "depth": 7}
							if obj[8]<=3.357526315789474:
								# {"feature": "chlorides", "instances": 102, "metric_value": 0.1392, "depth": 8}
								if obj[4]<=0.08254901960784314:
									return 'good'
								elif obj[4]>0.08254901960784314:
									# {"feature": "free sulfur dioxide", "instances": 38, "metric_value": 0.2975, "depth": 9}
									if obj[5]>3.0:
										# {"feature": "total sulfur dioxide", "instances": 31, "metric_value": 0.3451, "depth": 10}
										if obj[6]>13.0:
											# {"feature": "density", "instances": 26, "metric_value": 0.2352, "depth": 11}
											if obj[7]>0.997:
												return 'good'
											elif obj[7]<=0.997:
												return 'good'
											else: return 'good'
										elif obj[6]<=13.0:
											# {"feature": "density", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[7]<=0.99664:
												return 'good'
											elif obj[7]>0.99664:
												return 'bad'
											else: return 'bad'
										else: return 'good'
									elif obj[5]<=3.0:
										return 'good'
									else: return 'good'
								else: return 'good'
							elif obj[8]>3.357526315789474:
								# {"feature": "total sulfur dioxide", "instances": 88, "metric_value": 0.5746, "depth": 8}
								if obj[6]<=95.40759928801877:
									# {"feature": "free sulfur dioxide", "instances": 83, "metric_value": 0.5307, "depth": 9}
									if obj[5]<=15.602409638554217:
										# {"feature": "density", "instances": 47, "metric_value": 0.7046, "depth": 10}
										if obj[7]<=0.9986511897778907:
											# {"feature": "chlorides", "instances": 46, "metric_value": 0.6666, "depth": 11}
											if obj[4]>0.039:
												return 'good'
											elif obj[4]<=0.039:
												return 'good'
											else: return 'good'
										elif obj[7]>0.9986511897778907:
											return 'bad'
										else: return 'bad'
									elif obj[5]>15.602409638554217:
										# {"feature": "density", "instances": 36, "metric_value": 0.1831, "depth": 10}
										if obj[7]<=0.9944411111111111:
											# {"feature": "chlorides", "instances": 20, "metric_value": 0.2864, "depth": 11}
											if obj[4]<=0.064:
												return 'good'
											elif obj[4]>0.064:
												return 'good'
											else: return 'good'
										elif obj[7]>0.9944411111111111:
											return 'good'
										else: return 'good'
									else: return 'good'
								elif obj[6]>95.40759928801877:
									# {"feature": "density", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[7]<=0.9932:
										return 'good'
									elif obj[7]>0.9932:
										return 'bad'
									else: return 'bad'
								else: return 'good'
							else: return 'good'
						elif obj[3]>7.040785216351962:
							# {"feature": "chlorides", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[4]<=0.051:
								return 'good'
							elif obj[4]>0.051:
								return 'bad'
							else: return 'bad'
						else: return 'good'
					elif obj[1]>0.987688211146936:
						# {"feature": "residual sugar", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]<=1.6:
							return 'bad'
						elif obj[3]>1.6:
							return 'good'
						else: return 'good'
					else: return 'bad'
				elif obj[9]<=0.37:
					return 'bad'
				else: return 'bad'
			elif obj[2]>0.7379684184330622:
				return 'bad'
			else: return 'bad'
		elif obj[0]>13.920456847074043:
			return 'bad'
		else: return 'bad'
	else: return 'good'
