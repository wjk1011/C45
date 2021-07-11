def findDecision(obj): #obj[0]: fixed acidity, obj[1]: volatile acidity, obj[2]: citric acid, obj[3]: residual sugar, obj[4]: chlorides, obj[5]: free sulfur dioxide, obj[6]: total sulfur dioxide, obj[7]: density, obj[8]: pH, obj[9]: sulphates, obj[10]: alcohol
	# {"feature": "alcohol", "instances": 1199, "metric_value": 0.9947, "depth": 1}
	if obj[10]<=11.520595666936513:
		# {"feature": "total sulfur dioxide", "instances": 1003, "metric_value": 0.9977, "depth": 2}
		if obj[6]<=110.97013851884896:
			# {"feature": "volatile acidity", "instances": 947, "metric_value": 0.9999, "depth": 3}
			if obj[1]<=1.0855516022267968:
				# {"feature": "chlorides", "instances": 941, "metric_value": 1.0, "depth": 4}
				if obj[4]>0.038:
					# {"feature": "free sulfur dioxide", "instances": 939, "metric_value": 1.0, "depth": 5}
					if obj[5]>1.0:
						# {"feature": "fixed acidity", "instances": 937, "metric_value": 1.0, "depth": 6}
						if obj[0]>5.0:
							# {"feature": "density", "instances": 935, "metric_value": 1.0, "depth": 7}
							if obj[7]>0.9929399999999999:
								# {"feature": "citric acid", "instances": 934, "metric_value": 1.0, "depth": 8}
								if obj[2]<=0.8311235901056224:
									# {"feature": "pH", "instances": 933, "metric_value": 1.0, "depth": 9}
									if obj[8]>2.87:
										# {"feature": "sulphates", "instances": 932, "metric_value": 1.0, "depth": 10}
										if obj[9]>0.33:
											# {"feature": "residual sugar", "instances": 931, "metric_value": 1.0, "depth": 11}
											if obj[3]<=6.13665243558791:
												return 'bad'
											elif obj[3]>6.13665243558791:
												return 'good'
											else: return 'good'
										elif obj[9]<=0.33:
											return 'bad'
										else: return 'bad'
									elif obj[8]<=2.87:
										return 'good'
									else: return 'good'
								elif obj[2]>0.8311235901056224:
									return 'bad'
								else: return 'bad'
							elif obj[7]<=0.9929399999999999:
								return 'good'
							else: return 'good'
						elif obj[0]<=5.0:
							return 'bad'
						else: return 'bad'
					elif obj[5]<=1.0:
						return 'good'
					else: return 'good'
				elif obj[4]<=0.038:
					return 'good'
				else: return 'good'
			elif obj[1]>1.0855516022267968:
				return 'bad'
			else: return 'bad'
		elif obj[6]>110.97013851884896:
			# {"feature": "density", "instances": 56, "metric_value": 0.3712, "depth": 3}
			if obj[7]>0.994841359540454:
				# {"feature": "pH", "instances": 54, "metric_value": 0.2285, "depth": 4}
				if obj[8]>2.93:
					return 'bad'
				elif obj[8]<=2.93:
					return 'good'
				else: return 'good'
			elif obj[7]<=0.994841359540454:
				return 'good'
			else: return 'good'
		else: return 'bad'
	elif obj[10]>11.520595666936513:
		# {"feature": "fixed acidity", "instances": 196, "metric_value": 0.4426, "depth": 2}
		if obj[0]>4.6:
			# {"feature": "sulphates", "instances": 195, "metric_value": 0.427, "depth": 3}
			if obj[9]>0.37:
				# {"feature": "citric acid", "instances": 194, "metric_value": 0.4108, "depth": 4}
				if obj[2]<=0.7585671586369825:
					# {"feature": "residual sugar", "instances": 192, "metric_value": 0.3955, "depth": 5}
					if obj[3]<=7.0518610175683865:
						# {"feature": "volatile acidity", "instances": 187, "metric_value": 0.3641, "depth": 6}
						if obj[1]<=0.6135414928667066:
							# {"feature": "pH", "instances": 154, "metric_value": 0.2375, "depth": 7}
							if obj[8]<=3.4774255171430775:
								# {"feature": "free sulfur dioxide", "instances": 135, "metric_value": 0.1925, "depth": 8}
								if obj[5]<=13.322222222222223:
									# {"feature": "chlorides", "instances": 90, "metric_value": 0.2623, "depth": 9}
									if obj[4]>0.05410455622704502:
										# {"feature": "total sulfur dioxide", "instances": 78, "metric_value": 0.172, "depth": 10}
										if obj[6]<=20.94871794871795:
											return 'good'
										elif obj[6]>20.94871794871795:
											# {"feature": "density", "instances": 34, "metric_value": 0.3228, "depth": 11}
											if obj[7]>0.9941779775559011:
												return 'good'
											elif obj[7]<=0.9941779775559011:
												return 'good'
											else: return 'good'
										else: return 'good'
									elif obj[4]<=0.05410455622704502:
										# {"feature": "total sulfur dioxide", "instances": 12, "metric_value": 0.65, "depth": 10}
										if obj[6]<=27.0:
											# {"feature": "density", "instances": 11, "metric_value": 0.4395, "depth": 11}
											if obj[7]<=0.995:
												return 'good'
											elif obj[7]>0.995:
												return 'good'
											else: return 'good'
										elif obj[6]>27.0:
											return 'bad'
										else: return 'bad'
									else: return 'good'
								elif obj[5]>13.322222222222223:
									return 'good'
								else: return 'good'
							elif obj[8]>3.4774255171430775:
								# {"feature": "free sulfur dioxide", "instances": 19, "metric_value": 0.4855, "depth": 8}
								if obj[5]>12.0:
									# {"feature": "total sulfur dioxide", "instances": 17, "metric_value": 0.3228, "depth": 9}
									if obj[6]<=89.0:
										return 'good'
									elif obj[6]>89.0:
										# {"feature": "chlorides", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[4]>0.049:
											return 'good'
										elif obj[4]<=0.049:
											return 'bad'
										else: return 'bad'
									else: return 'good'
								elif obj[5]<=12.0:
									# {"feature": "chlorides", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[4]<=0.042:
										return 'good'
									elif obj[4]>0.042:
										return 'bad'
									else: return 'bad'
								else: return 'bad'
							else: return 'good'
						elif obj[1]>0.6135414928667066:
							# {"feature": "free sulfur dioxide", "instances": 33, "metric_value": 0.7455, "depth": 7}
							if obj[5]<=28.0:
								# {"feature": "chlorides", "instances": 27, "metric_value": 0.8256, "depth": 8}
								if obj[4]>0.07088888888888889:
									# {"feature": "density", "instances": 14, "metric_value": 0.3712, "depth": 9}
									if obj[7]>0.9953799999999999:
										return 'good'
									elif obj[7]<=0.9953799999999999:
										# {"feature": "total sulfur dioxide", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[6]>16.0:
											# {"feature": "pH", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[8]>3.57:
												return 'good'
											elif obj[8]<=3.57:
												return 'bad'
											else: return 'bad'
										elif obj[6]<=16.0:
											return 'good'
										else: return 'good'
									else: return 'good'
								elif obj[4]<=0.07088888888888889:
									# {"feature": "density", "instances": 13, "metric_value": 0.9957, "depth": 9}
									if obj[7]<=0.9933200000000001:
										# {"feature": "total sulfur dioxide", "instances": 8, "metric_value": 0.5436, "depth": 10}
										if obj[6]>15.0:
											return 'good'
										elif obj[6]<=15.0:
											# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[8]>3.47:
												return 'bad'
											elif obj[8]<=3.47:
												return 'good'
											else: return 'good'
										else: return 'bad'
									elif obj[7]>0.9933200000000001:
										return 'bad'
									else: return 'bad'
								else: return 'good'
							elif obj[5]>28.0:
								return 'good'
							else: return 'good'
						else: return 'good'
					elif obj[3]>7.0518610175683865:
						# {"feature": "chlorides", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[4]<=0.051:
							return 'good'
						elif obj[4]>0.051:
							return 'bad'
						else: return 'bad'
					else: return 'good'
				elif obj[2]>0.7585671586369825:
					# {"feature": "volatile acidity", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=0.37:
						return 'good'
					elif obj[1]>0.37:
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
