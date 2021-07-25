def findDecision(obj): #obj[0]: fixedacidity, obj[1]: volatileacidity, obj[2]: citricacid, obj[3]: residualsugar, obj[4]: chlorides, obj[5]: freesulfurdioxide, obj[6]: totalsulfurdioxide, obj[7]: density, obj[8]: pH, obj[9]: sulphates, obj[10]: alcohol, obj[11]: Decision
	# {"feature": "alcohol", "instances": 1122, "metric_value": 0.9979, "depth": 1}
	if obj[10]>11.420750561281332:
		# {"feature": "fixedacidity", "instances": 187, "metric_value": 0.3838, "depth": 2}
		if obj[0]<=4.6:
			return 'bad'
		elif obj[0]>4.6:
			# {"feature": "density", "instances": 186, "metric_value": 0.3655, "depth": 3}
			if obj[7]>0.9915664832460218:
				# {"feature": "totalsulfurdioxide", "instances": 179, "metric_value": 0.3756, "depth": 4}
				if obj[6]>115.46693969368832:
					return 'good'
				elif obj[6]<=115.46693969368832:
					# {"feature": "volatileacidity", "instances": 176, "metric_value": 0.3802, "depth": 5}
					if obj[1]<=1.0578427006423825:
						# {"feature": "citricacid", "instances": 176, "metric_value": 0.3802, "depth": 6}
						if obj[2]<=0.8920604764329993:
							# {"feature": "residualsugar", "instances": 176, "metric_value": 0.3802, "depth": 7}
							if obj[3]>0.9:
								# {"feature": "chlorides", "instances": 176, "metric_value": 0.3802, "depth": 8}
								if obj[4]>0.012:
									# {"feature": "freesulfurdioxide", "instances": 176, "metric_value": 0.3802, "depth": 9}
									if obj[5]>1.0:
										# {"feature": "pH", "instances": 176, "metric_value": 0.3802, "depth": 10}
										if obj[8]>2.74:
											# {"feature": "sulphates", "instances": 176, "metric_value": 0.3802, "depth": 11}
											if obj[9]>0.33:
												return 'good'
											else: return 'good'
										else: return 'good'
									else: return 'good'
								else: return 'good'
							else: return 'good'
						else: return 'good'
					else: return 'good'
				else: return 'good'
			elif obj[7]<=0.9915664832460218:
				return 'good'
			else: return 'good'
		else: return 'good'
	elif obj[10]<=11.420750561281332:
		# {"feature": "freesulfurdioxide", "instances": 935, "metric_value": 0.9919, "depth": 2}
		if obj[5]<=1.0:
			return 'good'
		elif obj[5]>1.0:
			# {"feature": "totalsulfurdioxide", "instances": 932, "metric_value": 0.9913, "depth": 3}
			if obj[6]<=115.46693969368832:
				# {"feature": "volatileacidity", "instances": 876, "metric_value": 0.9975, "depth": 4}
				if obj[1]>1.0578427006423825:
					return 'bad'
				elif obj[1]<=1.0578427006423825:
					# {"feature": "citricacid", "instances": 869, "metric_value": 0.9981, "depth": 5}
					if obj[2]<=0.8920604764329993:
						# {"feature": "sulphates", "instances": 868, "metric_value": 0.9981, "depth": 6}
						if obj[9]<=0.33:
							return 'bad'
						elif obj[9]>0.33:
							# {"feature": "fixedacidity", "instances": 867, "metric_value": 0.9982, "depth": 7}
							if obj[0]>4.6:
								# {"feature": "residualsugar", "instances": 867, "metric_value": 0.9982, "depth": 8}
								if obj[3]>0.9:
									# {"feature": "chlorides", "instances": 867, "metric_value": 0.9982, "depth": 9}
									if obj[4]>0.012:
										# {"feature": "density", "instances": 867, "metric_value": 0.9982, "depth": 10}
										if obj[7]>0.9915664832460218:
											# {"feature": "pH", "instances": 867, "metric_value": 0.9982, "depth": 11}
											if obj[8]>2.74:
												return 'good'
											else: return 'good'
										else: return 'good'
									else: return 'good'
								else: return 'good'
							else: return 'good'
						else: return 'good'
					elif obj[2]>0.8920604764329993:
						return 'bad'
					else: return 'bad'
				else: return 'good'
			elif obj[6]>115.46693969368832:
				# {"feature": "volatileacidity", "instances": 56, "metric_value": 0.3014, "depth": 4}
				if obj[1]>1.0578427006423825:
					return 'bad'
				elif obj[1]<=1.0578427006423825:
					# {"feature": "fixedacidity", "instances": 55, "metric_value": 0.3054, "depth": 5}
					if obj[0]>4.6:
						# {"feature": "citricacid", "instances": 55, "metric_value": 0.3054, "depth": 6}
						if obj[2]<=0.8920604764329993:
							# {"feature": "residualsugar", "instances": 55, "metric_value": 0.3054, "depth": 7}
							if obj[3]>0.9:
								# {"feature": "chlorides", "instances": 55, "metric_value": 0.3054, "depth": 8}
								if obj[4]>0.012:
									# {"feature": "density", "instances": 55, "metric_value": 0.3054, "depth": 9}
									if obj[7]>0.9915664832460218:
										# {"feature": "pH", "instances": 55, "metric_value": 0.3054, "depth": 10}
										if obj[8]>2.74:
											# {"feature": "sulphates", "instances": 55, "metric_value": 0.3054, "depth": 11}
											if obj[9]>0.33:
												return 'good'
											else: return 'good'
										else: return 'good'
									else: return 'good'
								else: return 'good'
							else: return 'good'
						else: return 'good'
					else: return 'good'
				else: return 'good'
			else: return 'good'
		else: return 'good'
	else: return 'bad'
