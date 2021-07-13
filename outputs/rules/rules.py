def findDecision(obj): #obj[0]: fixed acidity, obj[1]: volatile acidity, obj[2]: citric acid, obj[3]: residual sugar, obj[4]: chlorides, obj[5]: free sulfur dioxide, obj[6]: total sulfur dioxide, obj[7]: density, obj[8]: pH, obj[9]: sulphates, obj[10]: alcohol
	# {"feature": "alcohol", "instances": 1199, "metric_value": 0.996, "depth": 1}
	if obj[10]<=11.506187726324267:
		# {"feature": "volatile acidity", "instances": 1012, "metric_value": 0.9971, "depth": 2}
		if obj[1]<=1.0793545320067004:
			# {"feature": "free sulfur dioxide", "instances": 1005, "metric_value": 0.9977, "depth": 3}
			if obj[5]>1.0:
				# {"feature": "density", "instances": 1003, "metric_value": 0.9975, "depth": 4}
				if obj[7]>0.9923909424730946:
					# {"feature": "total sulfur dioxide", "instances": 1001, "metric_value": 0.9973, "depth": 5}
					if obj[6]<=112.65197391662508:
						# {"feature": "fixed acidity", "instances": 942, "metric_value": 0.9999, "depth": 6}
						if obj[0]>5.0:
							# {"feature": "citric acid", "instances": 941, "metric_value": 0.9999, "depth": 7}
							if obj[2]<=0.8423382707361093:
								# {"feature": "pH", "instances": 940, "metric_value": 0.9999, "depth": 8}
								if obj[8]>2.86:
									# {"feature": "chlorides", "instances": 939, "metric_value": 0.9999, "depth": 9}
									if obj[4]>0.039:
										# {"feature": "sulphates", "instances": 938, "metric_value": 0.9999, "depth": 10}
										if obj[9]>0.33:
											# {"feature": "residual sugar", "instances": 937, "metric_value": 1.0, "depth": 11}
											if obj[3]<=5.952799729877089:
												return 'bad'
											elif obj[3]>5.952799729877089:
												return 'bad'
											else: return 'bad'
										elif obj[9]<=0.33:
											return 'bad'
										else: return 'bad'
									elif obj[4]<=0.039:
										return 'bad'
									else: return 'bad'
								elif obj[8]<=2.86:
									return 'good'
								else: return 'good'
							elif obj[2]>0.8423382707361093:
								return 'bad'
							else: return 'bad'
						elif obj[0]<=5.0:
							return 'bad'
						else: return 'bad'
					elif obj[6]>112.65197391662508:
						# {"feature": "residual sugar", "instances": 59, "metric_value": 0.3576, "depth": 6}
						if obj[3]<=7.2780611948496094:
							# {"feature": "pH", "instances": 57, "metric_value": 0.2193, "depth": 7}
							if obj[8]>2.93:
								return 'bad'
							elif obj[8]<=2.93:
								# {"feature": "citric acid", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2]<=0.28:
									return 'good'
								elif obj[2]>0.28:
									return 'bad'
								else: return 'bad'
							else: return 'good'
						elif obj[3]>7.2780611948496094:
							return 'good'
						else: return 'good'
					else: return 'bad'
				elif obj[7]<=0.9923909424730946:
					return 'good'
				else: return 'good'
			elif obj[5]<=1.0:
				return 'good'
			else: return 'good'
		elif obj[1]>1.0793545320067004:
			return 'bad'
		else: return 'bad'
	elif obj[10]>11.506187726324267:
		# {"feature": "fixed acidity", "instances": 187, "metric_value": 0.4395, "depth": 2}
		if obj[0]>4.6:
			# {"feature": "total sulfur dioxide", "instances": 186, "metric_value": 0.423, "depth": 3}
			if obj[6]>7.0:
				# {"feature": "citric acid", "instances": 185, "metric_value": 0.406, "depth": 4}
				if obj[2]<=0.7369158145927215:
					# {"feature": "residual sugar", "instances": 183, "metric_value": 0.3897, "depth": 5}
					if obj[3]<=6.886791665033607:
						# {"feature": "pH", "instances": 178, "metric_value": 0.3562, "depth": 6}
						if obj[8]<=3.3645505617977536:
							return 'good'
						elif obj[8]>3.3645505617977536:
							# {"feature": "sulphates", "instances": 73, "metric_value": 0.6447, "depth": 7}
							if obj[9]>0.5370425628439339:
								# {"feature": "volatile acidity", "instances": 62, "metric_value": 0.5086, "depth": 8}
								if obj[1]<=0.6989145565524779:
									# {"feature": "density", "instances": 50, "metric_value": 0.5842, "depth": 9}
									if obj[7]>0.9920241406713305:
										# {"feature": "free sulfur dioxide", "instances": 41, "metric_value": 0.6594, "depth": 10}
										if obj[5]<=19.0:
											# {"feature": "chlorides", "instances": 35, "metric_value": 0.7219, "depth": 11}
											if obj[4]>0.034:
												return 'good'
											elif obj[4]<=0.034:
												return 'good'
											else: return 'good'
										elif obj[5]>19.0:
											return 'good'
										else: return 'good'
									elif obj[7]<=0.9920241406713305:
										return 'good'
									else: return 'good'
								elif obj[1]>0.6989145565524779:
									return 'good'
								else: return 'good'
							elif obj[9]<=0.5370425628439339:
								# {"feature": "chlorides", "instances": 11, "metric_value": 0.994, "depth": 8}
								if obj[4]>0.053:
									# {"feature": "free sulfur dioxide", "instances": 9, "metric_value": 0.9183, "depth": 9}
									if obj[5]<=27.0:
										# {"feature": "density", "instances": 8, "metric_value": 0.8113, "depth": 10}
										if obj[7]>0.99242:
											# {"feature": "volatile acidity", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[1]>0.36:
												return 'good'
											elif obj[1]<=0.36:
												return 'good'
											else: return 'good'
										elif obj[7]<=0.99242:
											return 'good'
										else: return 'good'
									elif obj[5]>27.0:
										return 'bad'
									else: return 'bad'
								elif obj[4]<=0.053:
									return 'bad'
								else: return 'bad'
							else: return 'good'
						else: return 'good'
					elif obj[3]>6.886791665033607:
						# {"feature": "chlorides", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[4]<=0.051:
							return 'good'
						elif obj[4]>0.051:
							return 'bad'
						else: return 'bad'
					else: return 'good'
				elif obj[2]>0.7369158145927215:
					# {"feature": "volatile acidity", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]>0.37:
						return 'bad'
					elif obj[1]<=0.37:
						return 'good'
					else: return 'good'
				else: return 'bad'
			elif obj[6]<=7.0:
				return 'bad'
			else: return 'bad'
		elif obj[0]<=4.6:
			return 'bad'
		else: return 'bad'
	else: return 'good'
