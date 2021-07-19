def findDecision(obj): #obj[0]: age, obj[1]: job, obj[2]: marital, obj[3]: education, obj[4]: default, obj[5]: housing, obj[6]: loan, obj[7]: contact, obj[8]: month, obj[9]: day_of_week, obj[10]: duration, obj[11]: campaign, obj[12]: pdays, obj[13]: previous, obj[14]: poutcome, obj[15]: emp.var.rate, obj[16]: cons.price.idx, obj[17]: cons.conf.idx, obj[18]: euribor3m, obj[19]: nr.employed
	# {"feature": "duration", "instances": 3940, "metric_value": 0.208, "depth": 1}
	if obj[10]<=772.3488414856213:
		# {"feature": "age", "instances": 3740, "metric_value": 0.0906, "depth": 2}
		if obj[0]>22.701558270454385:
			# {"feature": "marital", "instances": 3733, "metric_value": 0.0907, "depth": 3}
			if obj[2] == 'married':
				# {"feature": "campaign", "instances": 2518, "metric_value": 0.0907, "depth": 4}
				if obj[11]<=10.32683241574345:
					# {"feature": "job", "instances": 2475, "metric_value": 0.0894, "depth": 5}
					if obj[1] == 'blue-collar':
						# {"feature": "education", "instances": 832, "metric_value": 0.1089, "depth": 6}
						if obj[3] == 'basic.9y':
							# {"feature": "euribor3m", "instances": 325, "metric_value": 0.15, "depth": 7}
							if obj[18]<=4.859:
								# {"feature": "day_of_week", "instances": 296, "metric_value": 0.1236, "depth": 8}
								if obj[9] == 'wed':
									return 'no'
								elif obj[9] == 'tue':
									# {"feature": "default", "instances": 65, "metric_value": 0.1147, "depth": 9}
									if obj[4] == 'no':
										return 'no'
									elif obj[4] == 'unknown':
										# {"feature": "housing", "instances": 24, "metric_value": 0.2499, "depth": 10}
										if obj[5] == 'yes':
											return 'no'
										elif obj[5] == 'no':
											# {"feature": "loan", "instances": 11, "metric_value": 0.4395, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 10, "metric_value": 0.469, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 10, "metric_value": 0.469, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 10, "metric_value": 0.469, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 10, "metric_value": 0.469, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 10, "metric_value": 0.469, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 10, "metric_value": 0.469, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 10, "metric_value": 0.469, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 10, "metric_value": 0.469, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 10, "metric_value": 0.469, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[6] == 'yes':
												return 'no'
											else: return 'no'
										elif obj[5] == 'unknown':
											return 'no'
										else: return 'no'
									else: return 'no'
								elif obj[9] == 'mon':
									# {"feature": "loan", "instances": 59, "metric_value": 0.29, "depth": 9}
									if obj[6] == 'no':
										# {"feature": "default", "instances": 47, "metric_value": 0.2539, "depth": 10}
										if obj[4] == 'no':
											# {"feature": "housing", "instances": 28, "metric_value": 0.2223, "depth": 11}
											if obj[5] == 'yes':
												return 'no'
											elif obj[5] == 'no':
												# {"feature": "contact", "instances": 12, "metric_value": 0.4138, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 12, "metric_value": 0.4138, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 12, "metric_value": 0.4138, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 12, "metric_value": 0.4138, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 12, "metric_value": 0.4138, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 12, "metric_value": 0.4138, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 12, "metric_value": 0.4138, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 12, "metric_value": 0.4138, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 12, "metric_value": 0.4138, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										elif obj[4] == 'unknown':
											# {"feature": "housing", "instances": 19, "metric_value": 0.2975, "depth": 11}
											if obj[5] == 'no':
												return 'no'
											elif obj[5] == 'yes':
												# {"feature": "contact", "instances": 9, "metric_value": 0.5033, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 9, "metric_value": 0.5033, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 9, "metric_value": 0.5033, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 9, "metric_value": 0.5033, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 9, "metric_value": 0.5033, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 9, "metric_value": 0.5033, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 9, "metric_value": 0.5033, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 9, "metric_value": 0.5033, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 9, "metric_value": 0.5033, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										else: return 'no'
									elif obj[6] == 'yes':
										# {"feature": "default", "instances": 9, "metric_value": 0.5033, "depth": 10}
										if obj[4] == 'no':
											# {"feature": "housing", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[5] == 'yes':
												# {"feature": "contact", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 4, "metric_value": 0.8113, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[5] == 'no':
												return 'no'
											else: return 'no'
										elif obj[4] == 'unknown':
											return 'no'
										else: return 'no'
									elif obj[6] == 'unknown':
										return 'no'
									else: return 'no'
								elif obj[9] == 'fri':
									# {"feature": "loan", "instances": 57, "metric_value": 0.1274, "depth": 9}
									if obj[6] == 'no':
										return 'no'
									elif obj[6] == 'yes':
										# {"feature": "housing", "instances": 10, "metric_value": 0.469, "depth": 10}
										if obj[5] == 'yes':
											return 'no'
										elif obj[5] == 'no':
											# {"feature": "default", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[4] == 'no':
												# {"feature": "contact", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										else: return 'no'
									else: return 'no'
								elif obj[9] == 'thu':
									return 'no'
								else: return 'no'
							elif obj[18]>4.859:
								# {"feature": "default", "instances": 29, "metric_value": 0.3621, "depth": 8}
								if obj[4] == 'no':
									# {"feature": "loan", "instances": 18, "metric_value": 0.5033, "depth": 9}
									if obj[6] == 'no':
										# {"feature": "housing", "instances": 14, "metric_value": 0.5917, "depth": 10}
										if obj[5] == 'no':
											# {"feature": "contact", "instances": 9, "metric_value": 0.5033, "depth": 11}
											if obj[7] == 'telephone':
												# {"feature": "month", "instances": 9, "metric_value": 0.5033, "depth": 12}
												if obj[8] == 'may':
													# {"feature": "day_of_week", "instances": 9, "metric_value": 0.5033, "depth": 13}
													if obj[9] == 'thu':
														# {"feature": "pdays", "instances": 9, "metric_value": 0.5033, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 9, "metric_value": 0.5033, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 9, "metric_value": 0.5033, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 9, "metric_value": 0.5033, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 9, "metric_value": 0.5033, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 9, "metric_value": 0.5033, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 9, "metric_value": 0.5033, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										elif obj[5] == 'yes':
											# {"feature": "contact", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[7] == 'telephone':
												# {"feature": "month", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[8] == 'may':
													# {"feature": "day_of_week", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[9] == 'thu':
														# {"feature": "pdays", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 5, "metric_value": 0.7219, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 5, "metric_value": 0.7219, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 5, "metric_value": 0.7219, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 5, "metric_value": 0.7219, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 5, "metric_value": 0.7219, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										else: return 'no'
									elif obj[6] == 'yes':
										return 'no'
									elif obj[6] == 'unknown':
										return 'no'
									else: return 'no'
								elif obj[4] == 'unknown':
									return 'no'
								else: return 'no'
							else: return 'no'
						elif obj[3] == 'basic.4y':
							# {"feature": "euribor3m", "instances": 238, "metric_value": 0.0392, "depth": 7}
							if obj[18]>4.856:
								return 'no'
							elif obj[18]<=4.856:
								# {"feature": "default", "instances": 83, "metric_value": 0.0941, "depth": 8}
								if obj[4] == 'unknown':
									# {"feature": "housing", "instances": 49, "metric_value": 0.1437, "depth": 9}
									if obj[5] == 'no':
										# {"feature": "day_of_week", "instances": 25, "metric_value": 0.2423, "depth": 10}
										if obj[9] == 'tue':
											# {"feature": "loan", "instances": 13, "metric_value": 0.3912, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 10, "metric_value": 0.469, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 10, "metric_value": 0.469, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 10, "metric_value": 0.469, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 10, "metric_value": 0.469, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 10, "metric_value": 0.469, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 10, "metric_value": 0.469, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 10, "metric_value": 0.469, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 10, "metric_value": 0.469, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 10, "metric_value": 0.469, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[6] == 'yes':
												return 'no'
											else: return 'no'
										elif obj[9] == 'thu':
											return 'no'
										elif obj[9] == 'fri':
											return 'no'
										elif obj[9] == 'wed':
											return 'no'
										else: return 'no'
									elif obj[5] == 'yes':
										return 'no'
									elif obj[5] == 'unknown':
										return 'no'
									else: return 'no'
								elif obj[4] == 'no':
									return 'no'
								else: return 'no'
							else: return 'no'
						elif obj[3] == 'basic.6y':
							# {"feature": "housing", "instances": 143, "metric_value": 0.1469, "depth": 7}
							if obj[5] == 'no':
								return 'no'
							elif obj[5] == 'yes':
								# {"feature": "euribor3m", "instances": 62, "metric_value": 0.2056, "depth": 8}
								if obj[18]>4.856:
									# {"feature": "day_of_week", "instances": 32, "metric_value": 0.3373, "depth": 9}
									if obj[9] == 'mon':
										return 'no'
									elif obj[9] == 'wed':
										# {"feature": "default", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[4] == 'no':
											return 'no'
										elif obj[4] == 'unknown':
											# {"feature": "loan", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=5191:
																					return 'yes'
																				else: return 'yes'
																			else: return 'yes'
																		else: return 'yes'
																	else: return 'yes'
																else: return 'yes'
															else: return 'yes'
														else: return 'yes'
													else: return 'yes'
												else: return 'yes'
											elif obj[6] == 'yes':
												return 'no'
											else: return 'no'
										else: return 'no'
									elif obj[9] == 'fri':
										# {"feature": "default", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[4] == 'no':
											# {"feature": "loan", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										elif obj[4] == 'unknown':
											return 'no'
										else: return 'no'
									elif obj[9] == 'thu':
										return 'no'
									elif obj[9] == 'tue':
										return 'no'
									else: return 'no'
								elif obj[18]<=4.856:
									return 'no'
								else: return 'no'
							elif obj[5] == 'unknown':
								# {"feature": "euribor3m", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[18]<=4.8580000000000005:
									return 'no'
								elif obj[18]>4.8580000000000005:
									return 'yes'
								else: return 'yes'
							else: return 'no'
						elif obj[3] == 'high.school':
							return 'no'
						elif obj[3] == 'unknown':
							return 'no'
						elif obj[3] == 'professional.course':
							# {"feature": "loan", "instances": 40, "metric_value": 0.1687, "depth": 7}
							if obj[6] == 'no':
								return 'no'
							elif obj[6] == 'yes':
								# {"feature": "euribor3m", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[18]>4.855:
									return 'no'
								elif obj[18]<=4.855:
									# {"feature": "day_of_week", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[9] == 'fri':
										return 'yes'
									elif obj[9] == 'thu':
										return 'no'
									else: return 'no'
								else: return 'yes'
							else: return 'no'
						elif obj[3] == 'university.degree':
							return 'no'
						else: return 'no'
					elif obj[1] == 'admin.':
						# {"feature": "default", "instances": 403, "metric_value": 0.0803, "depth": 6}
						if obj[4] == 'no':
							# {"feature": "day_of_week", "instances": 325, "metric_value": 0.0957, "depth": 7}
							if obj[9] == 'tue':
								# {"feature": "housing", "instances": 79, "metric_value": 0.0979, "depth": 8}
								if obj[5] == 'no':
									# {"feature": "euribor3m", "instances": 39, "metric_value": 0.172, "depth": 9}
									if obj[18]<=4.856:
										# {"feature": "education", "instances": 23, "metric_value": 0.258, "depth": 10}
										if obj[3] == 'high.school':
											# {"feature": "loan", "instances": 11, "metric_value": 0.4395, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 9, "metric_value": 0.5033, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 9, "metric_value": 0.5033, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 9, "metric_value": 0.5033, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 9, "metric_value": 0.5033, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 9, "metric_value": 0.5033, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 9, "metric_value": 0.5033, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 9, "metric_value": 0.5033, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 9, "metric_value": 0.5033, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 9, "metric_value": 0.5033, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[6] == 'yes':
												return 'no'
											else: return 'no'
										elif obj[3] == 'university.degree':
											return 'no'
										elif obj[3] == 'basic.6y':
											return 'no'
										elif obj[3] == 'basic.9y':
											return 'no'
										elif obj[3] == 'unknown':
											return 'no'
										elif obj[3] == 'basic.4y':
											return 'no'
										else: return 'no'
									elif obj[18]>4.856:
										return 'no'
									else: return 'no'
								elif obj[5] == 'yes':
									return 'no'
								elif obj[5] == 'unknown':
									return 'no'
								else: return 'no'
							elif obj[9] == 'fri':
								return 'no'
							elif obj[9] == 'wed':
								return 'no'
							elif obj[9] == 'mon':
								# {"feature": "housing", "instances": 61, "metric_value": 0.1207, "depth": 8}
								if obj[5] == 'no':
									# {"feature": "euribor3m", "instances": 33, "metric_value": 0.1959, "depth": 9}
									if obj[18]<=4.857:
										# {"feature": "education", "instances": 21, "metric_value": 0.2762, "depth": 10}
										if obj[3] == 'university.degree':
											# {"feature": "loan", "instances": 7, "metric_value": 0.5917, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 5, "metric_value": 0.7219, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 5, "metric_value": 0.7219, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 5, "metric_value": 0.7219, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 5, "metric_value": 0.7219, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 5, "metric_value": 0.7219, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[6] == 'yes':
												return 'no'
											else: return 'no'
										elif obj[3] == 'high.school':
											return 'no'
										elif obj[3] == 'unknown':
											return 'no'
										elif obj[3] == 'basic.6y':
											return 'no'
										elif obj[3] == 'basic.9y':
											return 'no'
										elif obj[3] == 'professional.course':
											return 'no'
										else: return 'no'
									elif obj[18]>4.857:
										return 'no'
									else: return 'no'
								elif obj[5] == 'yes':
									return 'no'
								elif obj[5] == 'unknown':
									return 'no'
								else: return 'no'
							elif obj[9] == 'thu':
								# {"feature": "loan", "instances": 54, "metric_value": 0.2285, "depth": 8}
								if obj[6] == 'no':
									# {"feature": "education", "instances": 42, "metric_value": 0.2762, "depth": 9}
									if obj[3] == 'university.degree':
										# {"feature": "euribor3m", "instances": 19, "metric_value": 0.2975, "depth": 10}
										if obj[18]>4.855:
											return 'no'
										elif obj[18]<=4.855:
											# {"feature": "housing", "instances": 8, "metric_value": 0.5436, "depth": 11}
											if obj[5] == 'no':
												# {"feature": "contact", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 5, "metric_value": 0.7219, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 5, "metric_value": 0.7219, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 5, "metric_value": 0.7219, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 5, "metric_value": 0.7219, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 5, "metric_value": 0.7219, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[5] == 'yes':
												return 'no'
											else: return 'no'
										else: return 'no'
									elif obj[3] == 'high.school':
										# {"feature": "euribor3m", "instances": 16, "metric_value": 0.3373, "depth": 10}
										if obj[18]<=4.855:
											return 'no'
										elif obj[18]>4.855:
											# {"feature": "housing", "instances": 7, "metric_value": 0.5917, "depth": 11}
											if obj[5] == 'yes':
												# {"feature": "contact", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 4, "metric_value": 0.8113, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[5] == 'no':
												return 'no'
											else: return 'no'
										else: return 'no'
									elif obj[3] == 'basic.6y':
										return 'no'
									elif obj[3] == 'unknown':
										return 'no'
									elif obj[3] == 'professional.course':
										return 'no'
									else: return 'no'
								elif obj[6] == 'yes':
									return 'no'
								elif obj[6] == 'unknown':
									return 'no'
								else: return 'no'
							else: return 'no'
						elif obj[4] == 'unknown':
							return 'no'
						else: return 'no'
					elif obj[1] == 'technician':
						# {"feature": "housing", "instances": 336, "metric_value": 0.1116, "depth": 6}
						if obj[5] == 'no':
							return 'no'
						elif obj[5] == 'yes':
							# {"feature": "euribor3m", "instances": 156, "metric_value": 0.2046, "depth": 7}
							if obj[18]<=4.8580000000000005:
								# {"feature": "education", "instances": 126, "metric_value": 0.2408, "depth": 8}
								if obj[3] == 'professional.course':
									# {"feature": "day_of_week", "instances": 66, "metric_value": 0.1959, "depth": 9}
									if obj[9] == 'tue':
										return 'no'
									elif obj[9] == 'wed':
										return 'no'
									elif obj[9] == 'mon':
										# {"feature": "loan", "instances": 13, "metric_value": 0.6194, "depth": 10}
										if obj[6] == 'no':
											# {"feature": "default", "instances": 10, "metric_value": 0.7219, "depth": 11}
											if obj[4] == 'no':
												# {"feature": "contact", "instances": 7, "metric_value": 0.5917, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 7, "metric_value": 0.5917, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 7, "metric_value": 0.5917, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 7, "metric_value": 0.5917, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 7, "metric_value": 0.5917, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 7, "metric_value": 0.5917, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 7, "metric_value": 0.5917, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 7, "metric_value": 0.5917, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 7, "metric_value": 0.5917, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[4] == 'unknown':
												# {"feature": "contact", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										elif obj[6] == 'yes':
											return 'no'
										else: return 'no'
									elif obj[9] == 'fri':
										return 'no'
									elif obj[9] == 'thu':
										return 'no'
									else: return 'no'
								elif obj[3] == 'university.degree':
									# {"feature": "day_of_week", "instances": 21, "metric_value": 0.2762, "depth": 9}
									if obj[9] == 'tue':
										# {"feature": "default", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[4] == 'no':
											# {"feature": "loan", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 4, "metric_value": 0.8113, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[6] == 'yes':
												return 'no'
											else: return 'no'
										elif obj[4] == 'unknown':
											return 'no'
										else: return 'no'
									elif obj[9] == 'fri':
										return 'no'
									elif obj[9] == 'mon':
										return 'no'
									elif obj[9] == 'thu':
										return 'no'
									elif obj[9] == 'wed':
										return 'no'
									else: return 'no'
								elif obj[3] == 'high.school':
									# {"feature": "day_of_week", "instances": 12, "metric_value": 0.65, "depth": 9}
									if obj[9] == 'wed':
										return 'no'
									elif obj[9] == 'mon':
										return 'no'
									elif obj[9] == 'tue':
										# {"feature": "default", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[4] == 'no':
											# {"feature": "loan", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=5191:
																					return 'yes'
																				else: return 'yes'
																			else: return 'yes'
																		else: return 'yes'
																	else: return 'yes'
																else: return 'yes'
															else: return 'yes'
														else: return 'yes'
													else: return 'yes'
												else: return 'yes'
											else: return 'yes'
										else: return 'yes'
									elif obj[9] == 'fri':
										return 'no'
									elif obj[9] == 'thu':
										return 'yes'
									else: return 'yes'
								elif obj[3] == 'basic.9y':
									return 'no'
								elif obj[3] == 'unknown':
									return 'no'
								elif obj[3] == 'basic.6y':
									return 'no'
								elif obj[3] == 'basic.4y':
									return 'no'
								else: return 'no'
							elif obj[18]>4.8580000000000005:
								return 'no'
							else: return 'no'
						elif obj[5] == 'unknown':
							return 'no'
						else: return 'no'
					elif obj[1] == 'services':
						# {"feature": "euribor3m", "instances": 286, "metric_value": 0.084, "depth": 6}
						if obj[18]<=4.8580000000000005:
							# {"feature": "day_of_week", "instances": 224, "metric_value": 0.1025, "depth": 7}
							if obj[9] == 'tue':
								return 'no'
							elif obj[9] == 'mon':
								# {"feature": "housing", "instances": 51, "metric_value": 0.1392, "depth": 8}
								if obj[5] == 'yes':
									# {"feature": "default", "instances": 26, "metric_value": 0.2352, "depth": 9}
									if obj[4] == 'no':
										# {"feature": "education", "instances": 15, "metric_value": 0.3534, "depth": 10}
										if obj[3] == 'high.school':
											# {"feature": "loan", "instances": 10, "metric_value": 0.469, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 8, "metric_value": 0.5436, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 8, "metric_value": 0.5436, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 8, "metric_value": 0.5436, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 8, "metric_value": 0.5436, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 8, "metric_value": 0.5436, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 8, "metric_value": 0.5436, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 8, "metric_value": 0.5436, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 8, "metric_value": 0.5436, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 8, "metric_value": 0.5436, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[6] == 'yes':
												return 'no'
											else: return 'no'
										elif obj[3] == 'basic.6y':
											return 'no'
										elif obj[3] == 'professional.course':
											return 'no'
										elif obj[3] == 'basic.9y':
											return 'no'
										else: return 'no'
									elif obj[4] == 'unknown':
										return 'no'
									else: return 'no'
								elif obj[5] == 'no':
									return 'no'
								elif obj[5] == 'unknown':
									return 'no'
								else: return 'no'
							elif obj[9] == 'wed':
								# {"feature": "loan", "instances": 44, "metric_value": 0.1565, "depth": 8}
								if obj[6] == 'no':
									return 'no'
								elif obj[6] == 'yes':
									# {"feature": "education", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[3] == 'high.school':
										# {"feature": "housing", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[5] == 'yes':
											# {"feature": "default", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[4] == 'no':
												# {"feature": "contact", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 4, "metric_value": 0.8113, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										elif obj[5] == 'no':
											return 'no'
										else: return 'no'
									elif obj[3] == 'basic.9y':
										return 'no'
									else: return 'no'
								elif obj[6] == 'unknown':
									return 'no'
								else: return 'no'
							elif obj[9] == 'fri':
								# {"feature": "default", "instances": 32, "metric_value": 0.2006, "depth": 8}
								if obj[4] == 'no':
									return 'no'
								elif obj[4] == 'unknown':
									# {"feature": "housing", "instances": 11, "metric_value": 0.4395, "depth": 9}
									if obj[5] == 'no':
										# {"feature": "education", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[3] == 'high.school':
											# {"feature": "loan", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 5, "metric_value": 0.7219, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 5, "metric_value": 0.7219, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 5, "metric_value": 0.7219, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 5, "metric_value": 0.7219, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 5, "metric_value": 0.7219, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[6] == 'yes':
												return 'no'
											else: return 'no'
										elif obj[3] == 'professional.course':
											return 'no'
										else: return 'no'
									elif obj[5] == 'yes':
										return 'no'
									else: return 'no'
								else: return 'no'
							elif obj[9] == 'thu':
								return 'no'
							else: return 'no'
						elif obj[18]>4.8580000000000005:
							return 'no'
						else: return 'no'
					elif obj[1] == 'management':
						# {"feature": "euribor3m", "instances": 195, "metric_value": 0.0825, "depth": 6}
						if obj[18]<=4.857:
							# {"feature": "default", "instances": 119, "metric_value": 0.1231, "depth": 7}
							if obj[4] == 'no':
								# {"feature": "education", "instances": 71, "metric_value": 0.1851, "depth": 8}
								if obj[3] == 'university.degree':
									# {"feature": "day_of_week", "instances": 44, "metric_value": 0.1565, "depth": 9}
									if obj[9] == 'tue':
										return 'no'
									elif obj[9] == 'mon':
										# {"feature": "housing", "instances": 10, "metric_value": 0.469, "depth": 10}
										if obj[5] == 'no':
											# {"feature": "loan", "instances": 8, "metric_value": 0.5436, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 8, "metric_value": 0.5436, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 8, "metric_value": 0.5436, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 8, "metric_value": 0.5436, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 8, "metric_value": 0.5436, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 8, "metric_value": 0.5436, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 8, "metric_value": 0.5436, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 8, "metric_value": 0.5436, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 8, "metric_value": 0.5436, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 8, "metric_value": 0.5436, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										elif obj[5] == 'yes':
											return 'no'
										else: return 'no'
									elif obj[9] == 'fri':
										return 'no'
									elif obj[9] == 'thu':
										return 'no'
									elif obj[9] == 'wed':
										return 'no'
									else: return 'no'
								elif obj[3] == 'high.school':
									return 'no'
								elif obj[3] == 'basic.9y':
									return 'no'
								elif obj[3] == 'basic.6y':
									return 'no'
								elif obj[3] == 'basic.4y':
									# {"feature": "loan", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[6] == 'no':
										return 'no'
									elif obj[6] == 'yes':
										return 'yes'
									else: return 'yes'
								elif obj[3] == 'professional.course':
									return 'no'
								elif obj[3] == 'unknown':
									return 'no'
								else: return 'no'
							elif obj[4] == 'unknown':
								return 'no'
							else: return 'no'
						elif obj[18]>4.857:
							return 'no'
						else: return 'no'
					elif obj[1] == 'entrepreneur':
						# {"feature": "loan", "instances": 106, "metric_value": 0.077, "depth": 6}
						if obj[6] == 'no':
							return 'no'
						elif obj[6] == 'yes':
							# {"feature": "euribor3m", "instances": 11, "metric_value": 0.4395, "depth": 7}
							if obj[18]<=4.8580000000000005:
								return 'no'
							elif obj[18]>4.8580000000000005:
								# {"feature": "housing", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[5] == 'no':
									return 'no'
								elif obj[5] == 'yes':
									return 'yes'
								else: return 'yes'
							else: return 'no'
						elif obj[6] == 'unknown':
							return 'no'
						else: return 'no'
					elif obj[1] == 'housemaid':
						# {"feature": "euribor3m", "instances": 79, "metric_value": 0.0979, "depth": 6}
						if obj[18]<=4.857:
							return 'no'
						elif obj[18]>4.857:
							# {"feature": "education", "instances": 29, "metric_value": 0.2164, "depth": 7}
							if obj[3] == 'basic.4y':
								# {"feature": "day_of_week", "instances": 10, "metric_value": 0.469, "depth": 8}
								if obj[9] == 'wed':
									# {"feature": "loan", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[6] == 'yes':
										return 'no'
									elif obj[6] == 'no':
										return 'yes'
									else: return 'yes'
								elif obj[9] == 'thu':
									return 'no'
								elif obj[9] == 'mon':
									return 'no'
								elif obj[9] == 'fri':
									return 'no'
								else: return 'no'
							elif obj[3] == 'high.school':
								return 'no'
							elif obj[3] == 'university.degree':
								return 'no'
							elif obj[3] == 'basic.9y':
								return 'no'
							elif obj[3] == 'basic.6y':
								return 'no'
							elif obj[3] == 'unknown':
								return 'no'
							else: return 'no'
						else: return 'no'
					elif obj[1] == 'self-employed':
						return 'no'
					elif obj[1] == 'retired':
						return 'no'
					elif obj[1] == 'unemployed':
						return 'no'
					elif obj[1] == 'unknown':
						return 'no'
					elif obj[1] == 'student':
						return 'no'
					else: return 'no'
				elif obj[11]>10.32683241574345:
					# {"feature": "euribor3m", "instances": 43, "metric_value": 0.1594, "depth": 5}
					if obj[18]<=4.859:
						return 'no'
					elif obj[18]>4.859:
						# {"feature": "job", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[1] == 'blue-collar':
							# {"feature": "education", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[3] == 'basic.9y':
								# {"feature": "default", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4] == 'no':
									# {"feature": "housing", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[5] == 'no':
										# {"feature": "loan", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6] == 'no':
											# {"feature": "contact", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7] == 'telephone':
												# {"feature": "month", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == 'may':
													# {"feature": "day_of_week", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'thu':
														# {"feature": "pdays", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=5191:
																					return 'yes'
																				else: return 'yes'
																			else: return 'yes'
																		else: return 'yes'
																	else: return 'yes'
																else: return 'yes'
															else: return 'yes'
														else: return 'yes'
													else: return 'yes'
												else: return 'yes'
											else: return 'yes'
										else: return 'yes'
									else: return 'yes'
								else: return 'yes'
							elif obj[3] == 'basic.4y':
								return 'no'
							else: return 'no'
						elif obj[1] == 'technician':
							return 'no'
						elif obj[1] == 'unemployed':
							return 'no'
						else: return 'no'
					else: return 'no'
				else: return 'no'
			elif obj[2] == 'single':
				# {"feature": "campaign", "instances": 770, "metric_value": 0.108, "depth": 4}
				if obj[11]<=3:
					# {"feature": "euribor3m", "instances": 642, "metric_value": 0.125, "depth": 5}
					if obj[18]<=4.859:
						# {"feature": "job", "instances": 585, "metric_value": 0.1347, "depth": 6}
						if obj[1] == 'admin.':
							# {"feature": "education", "instances": 174, "metric_value": 0.0905, "depth": 7}
							if obj[3] == 'university.degree':
								return 'no'
							elif obj[3] == 'high.school':
								# {"feature": "loan", "instances": 58, "metric_value": 0.1257, "depth": 8}
								if obj[6] == 'no':
									return 'no'
								elif obj[6] == 'yes':
									# {"feature": "day_of_week", "instances": 11, "metric_value": 0.4395, "depth": 9}
									if obj[9] == 'wed':
										return 'no'
									elif obj[9] == 'tue':
										# {"feature": "housing", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[5] == 'yes':
											# {"feature": "default", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[4] == 'no':
												# {"feature": "contact", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										elif obj[5] == 'no':
											return 'no'
										else: return 'no'
									elif obj[9] == 'mon':
										return 'no'
									elif obj[9] == 'thu':
										return 'no'
									else: return 'no'
								elif obj[6] == 'unknown':
									return 'no'
								else: return 'no'
							elif obj[3] == 'basic.9y':
								return 'no'
							elif obj[3] == 'basic.6y':
								return 'no'
							elif obj[3] == 'professional.course':
								# {"feature": "housing", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[5] == 'no':
									return 'no'
								elif obj[5] == 'yes':
									return 'yes'
								else: return 'yes'
							elif obj[3] == 'unknown':
								return 'no'
							elif obj[3] == 'basic.4y':
								return 'no'
							else: return 'no'
						elif obj[1] == 'blue-collar':
							# {"feature": "education", "instances": 122, "metric_value": 0.2829, "depth": 7}
							if obj[3] == 'basic.9y':
								# {"feature": "loan", "instances": 58, "metric_value": 0.3621, "depth": 8}
								if obj[6] == 'no':
									# {"feature": "day_of_week", "instances": 45, "metric_value": 0.4328, "depth": 9}
									if obj[9] == 'fri':
										# {"feature": "housing", "instances": 18, "metric_value": 0.3095, "depth": 10}
										if obj[5] == 'yes':
											return 'no'
										elif obj[5] == 'no':
											# {"feature": "default", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[4] == 'no':
												# {"feature": "contact", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 4, "metric_value": 0.8113, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[4] == 'unknown':
												return 'no'
											else: return 'no'
										else: return 'no'
									elif obj[9] == 'wed':
										# {"feature": "housing", "instances": 10, "metric_value": 0.469, "depth": 10}
										if obj[5] == 'no':
											return 'no'
										elif obj[5] == 'yes':
											# {"feature": "default", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[4] == 'unknown':
												# {"feature": "contact", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=5191:
																					return 'yes'
																				else: return 'yes'
																			else: return 'yes'
																		else: return 'yes'
																	else: return 'yes'
																else: return 'yes'
															else: return 'yes'
														else: return 'yes'
													else: return 'yes'
												else: return 'yes'
											elif obj[4] == 'no':
												return 'no'
											else: return 'no'
										else: return 'no'
									elif obj[9] == 'mon':
										return 'no'
									elif obj[9] == 'tue':
										# {"feature": "housing", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[5] == 'yes':
											return 'no'
										elif obj[5] == 'no':
											# {"feature": "default", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[4] == 'no':
												# {"feature": "contact", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										else: return 'no'
									elif obj[9] == 'thu':
										# {"feature": "housing", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[5] == 'no':
											return 'no'
										elif obj[5] == 'yes':
											return 'yes'
										else: return 'yes'
									else: return 'no'
								elif obj[6] == 'yes':
									return 'no'
								elif obj[6] == 'unknown':
									return 'no'
								else: return 'no'
							elif obj[3] == 'high.school':
								return 'no'
							elif obj[3] == 'basic.4y':
								return 'no'
							elif obj[3] == 'basic.6y':
								# {"feature": "default", "instances": 12, "metric_value": 0.4138, "depth": 8}
								if obj[4] == 'no':
									return 'no'
								elif obj[4] == 'unknown':
									# {"feature": "day_of_week", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[9] == 'fri':
										return 'yes'
									elif obj[9] == 'thu':
										return 'no'
									else: return 'no'
								else: return 'no'
							elif obj[3] == 'unknown':
								return 'no'
							elif obj[3] == 'university.degree':
								# {"feature": "housing", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[5] == 'yes':
									# {"feature": "default", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[4] == 'unknown':
										# {"feature": "loan", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6] == 'no':
											# {"feature": "contact", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7] == 'telephone':
												# {"feature": "month", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == 'may':
													# {"feature": "day_of_week", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'tue':
														# {"feature": "pdays", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=5191:
																					return 'yes'
																				else: return 'yes'
																			else: return 'yes'
																		else: return 'yes'
																	else: return 'yes'
																else: return 'yes'
															else: return 'yes'
														else: return 'yes'
													else: return 'yes'
												else: return 'yes'
											else: return 'yes'
										else: return 'yes'
									else: return 'yes'
								elif obj[5] == 'no':
									return 'no'
								else: return 'no'
							elif obj[3] == 'professional.course':
								return 'no'
							else: return 'no'
						elif obj[1] == 'technician':
							# {"feature": "day_of_week", "instances": 88, "metric_value": 0.0897, "depth": 7}
							if obj[9] == 'tue':
								return 'no'
							elif obj[9] == 'fri':
								return 'no'
							elif obj[9] == 'mon':
								return 'no'
							elif obj[9] == 'wed':
								# {"feature": "housing", "instances": 18, "metric_value": 0.3095, "depth": 8}
								if obj[5] == 'no':
									return 'no'
								elif obj[5] == 'yes':
									# {"feature": "education", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[3] == 'university.degree':
										# {"feature": "default", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[4] == 'no':
											# {"feature": "loan", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										elif obj[4] == 'unknown':
											return 'no'
										else: return 'no'
									elif obj[3] == 'professional.course':
										return 'no'
									elif obj[3] == 'high.school':
										return 'no'
									else: return 'no'
								elif obj[5] == 'unknown':
									return 'no'
								else: return 'no'
							elif obj[9] == 'thu':
								return 'no'
							else: return 'no'
						elif obj[1] == 'services':
							# {"feature": "default", "instances": 75, "metric_value": 0.1774, "depth": 7}
							if obj[4] == 'no':
								# {"feature": "loan", "instances": 56, "metric_value": 0.2223, "depth": 8}
								if obj[6] == 'no':
									# {"feature": "day_of_week", "instances": 42, "metric_value": 0.2762, "depth": 9}
									if obj[9] == 'wed':
										return 'no'
									elif obj[9] == 'mon':
										# {"feature": "housing", "instances": 11, "metric_value": 0.4395, "depth": 10}
										if obj[5] == 'yes':
											return 'no'
										elif obj[5] == 'no':
											# {"feature": "education", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[3] == 'high.school':
												# {"feature": "contact", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[3] == 'basic.9y':
												return 'no'
											elif obj[3] == 'basic.6y':
												return 'no'
											else: return 'no'
										else: return 'no'
									elif obj[9] == 'fri':
										# {"feature": "education", "instances": 10, "metric_value": 0.469, "depth": 10}
										if obj[3] == 'high.school':
											# {"feature": "housing", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[5] == 'yes':
												# {"feature": "contact", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[5] == 'no':
												return 'no'
											else: return 'no'
										elif obj[3] == 'basic.9y':
											return 'no'
										else: return 'no'
									elif obj[9] == 'tue':
										return 'no'
									elif obj[9] == 'thu':
										return 'no'
									else: return 'no'
								elif obj[6] == 'yes':
									return 'no'
								elif obj[6] == 'unknown':
									return 'no'
								else: return 'no'
							elif obj[4] == 'unknown':
								return 'no'
							else: return 'no'
						elif obj[1] == 'management':
							return 'no'
						elif obj[1] == 'self-employed':
							return 'no'
						elif obj[1] == 'student':
							return 'no'
						elif obj[1] == 'unemployed':
							return 'no'
						elif obj[1] == 'housemaid':
							return 'no'
						elif obj[1] == 'entrepreneur':
							return 'no'
						elif obj[1] == 'unknown':
							return 'no'
						elif obj[1] == 'retired':
							return 'no'
						else: return 'no'
					elif obj[18]>4.859:
						return 'no'
					else: return 'no'
				elif obj[11]>3:
					return 'no'
				else: return 'no'
			elif obj[2] == 'divorced':
				# {"feature": "campaign", "instances": 437, "metric_value": 0.0422, "depth": 4}
				if obj[11]<=4:
					# {"feature": "day_of_week", "instances": 395, "metric_value": 0.0255, "depth": 5}
					if obj[9] == 'fri':
						# {"feature": "housing", "instances": 86, "metric_value": 0.0914, "depth": 6}
						if obj[5] == 'yes':
							# {"feature": "education", "instances": 42, "metric_value": 0.1623, "depth": 7}
							if obj[3] == 'university.degree':
								# {"feature": "euribor3m", "instances": 10, "metric_value": 0.469, "depth": 8}
								if obj[18]<=4.857:
									# {"feature": "job", "instances": 7, "metric_value": 0.5917, "depth": 9}
									if obj[1] == 'admin.':
										# {"feature": "default", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[4] == 'no':
											# {"feature": "loan", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										else: return 'no'
									elif obj[1] == 'entrepreneur':
										return 'no'
									elif obj[1] == 'management':
										return 'no'
									elif obj[1] == 'unemployed':
										return 'no'
									else: return 'no'
								elif obj[18]>4.857:
									return 'no'
								else: return 'no'
							elif obj[3] == 'high.school':
								return 'no'
							elif obj[3] == 'basic.9y':
								return 'no'
							elif obj[3] == 'professional.course':
								return 'no'
							elif obj[3] == 'basic.4y':
								return 'no'
							elif obj[3] == 'basic.6y':
								return 'no'
							elif obj[3] == 'unknown':
								return 'no'
							else: return 'no'
						elif obj[5] == 'no':
							return 'no'
						elif obj[5] == 'unknown':
							return 'no'
						else: return 'no'
					elif obj[9] == 'mon':
						return 'no'
					elif obj[9] == 'wed':
						return 'no'
					elif obj[9] == 'tue':
						return 'no'
					elif obj[9] == 'thu':
						return 'no'
					else: return 'no'
				elif obj[11]>4:
					# {"feature": "day_of_week", "instances": 42, "metric_value": 0.1623, "depth": 5}
					if obj[9] == 'thu':
						return 'no'
					elif obj[9] == 'wed':
						return 'no'
					elif obj[9] == 'mon':
						# {"feature": "job", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[1] == 'admin.':
							return 'no'
						elif obj[1] == 'services':
							# {"feature": "education", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3] == 'professional.course':
								return 'no'
							elif obj[3] == 'high.school':
								return 'yes'
							else: return 'yes'
						elif obj[1] == 'entrepreneur':
							return 'no'
						elif obj[1] == 'technician':
							return 'no'
						elif obj[1] == 'management':
							return 'no'
						else: return 'no'
					elif obj[9] == 'tue':
						return 'no'
					elif obj[9] == 'fri':
						return 'no'
					else: return 'no'
				else: return 'no'
			elif obj[2] == 'unknown':
				# {"feature": "euribor3m", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[18]>4.855:
					return 'no'
				elif obj[18]<=4.855:
					return 'yes'
				else: return 'yes'
			else: return 'no'
		elif obj[0]<=22.701558270454385:
			return 'no'
		else: return 'no'
	elif obj[10]>772.3488414856213:
		# {"feature": "campaign", "instances": 200, "metric_value": 0.9858, "depth": 2}
		if obj[11]<=6:
			# {"feature": "loan", "instances": 194, "metric_value": 0.9907, "depth": 3}
			if obj[6] == 'no':
				# {"feature": "age", "instances": 157, "metric_value": 0.9816, "depth": 4}
				if obj[0]>24.002621701278:
					# {"feature": "job", "instances": 155, "metric_value": 0.9841, "depth": 5}
					if obj[1] == 'blue-collar':
						# {"feature": "education", "instances": 51, "metric_value": 0.9183, "depth": 6}
						if obj[3] == 'basic.9y':
							# {"feature": "day_of_week", "instances": 19, "metric_value": 0.8997, "depth": 7}
							if obj[9] == 'wed':
								# {"feature": "marital", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[2] == 'married':
									# {"feature": "housing", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[5] == 'no':
										return 'yes'
									elif obj[5] == 'yes':
										return 'no'
									else: return 'no'
								elif obj[2] == 'divorced':
									return 'no'
								elif obj[2] == 'single':
									return 'no'
								else: return 'no'
							elif obj[9] == 'fri':
								# {"feature": "marital", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[2] == 'divorced':
									return 'no'
								elif obj[2] == 'married':
									return 'no'
								elif obj[2] == 'single':
									return 'yes'
								else: return 'yes'
							elif obj[9] == 'tue':
								# {"feature": "marital", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2] == 'married':
									return 'no'
								elif obj[2] == 'single':
									return 'yes'
								else: return 'yes'
							elif obj[9] == 'mon':
								return 'no'
							elif obj[9] == 'thu':
								# {"feature": "default", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[4] == 'unknown':
									return 'yes'
								elif obj[4] == 'no':
									return 'no'
								else: return 'no'
							else: return 'yes'
						elif obj[3] == 'basic.4y':
							# {"feature": "marital", "instances": 14, "metric_value": 0.7496, "depth": 7}
							if obj[2] == 'married':
								# {"feature": "day_of_week", "instances": 12, "metric_value": 0.65, "depth": 8}
								if obj[9] == 'wed':
									# {"feature": "default", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[4] == 'unknown':
										# {"feature": "housing", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == 'yes':
											# {"feature": "contact", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7] == 'telephone':
												# {"feature": "month", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == 'may':
													# {"feature": "pdays", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[12]<=999:
														# {"feature": "previous", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13]<=0:
															# {"feature": "poutcome", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[14] == 'nonexistent':
																# {"feature": "emp.var.rate", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[15]<=1.1:
																	# {"feature": "cons.price.idx", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[16]<=93.994:
																		# {"feature": "cons.conf.idx", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17]<=-36.4:
																			# {"feature": "euribor3m", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[18]<=4.859:
																				# {"feature": "nr.employed", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=5191:
																					return 'yes'
																				else: return 'yes'
																			else: return 'yes'
																		else: return 'yes'
																	else: return 'yes'
																else: return 'yes'
															else: return 'yes'
														else: return 'yes'
													else: return 'yes'
												else: return 'yes'
											else: return 'yes'
										else: return 'yes'
									elif obj[4] == 'no':
										# {"feature": "housing", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == 'yes':
											# {"feature": "contact", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7] == 'telephone':
												# {"feature": "month", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == 'may':
													# {"feature": "pdays", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[12]<=999:
														# {"feature": "previous", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13]<=0:
															# {"feature": "poutcome", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[14] == 'nonexistent':
																# {"feature": "emp.var.rate", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[15]<=1.1:
																	# {"feature": "cons.price.idx", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[16]<=93.994:
																		# {"feature": "cons.conf.idx", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17]<=-36.4:
																			# {"feature": "euribor3m", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[18]<=4.856:
																				# {"feature": "nr.employed", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=5191:
																					return 'yes'
																				else: return 'yes'
																			else: return 'yes'
																		else: return 'yes'
																	else: return 'yes'
																else: return 'yes'
															else: return 'yes'
														else: return 'yes'
													else: return 'yes'
												else: return 'yes'
											else: return 'yes'
										else: return 'yes'
									else: return 'yes'
								elif obj[9] == 'mon':
									return 'no'
								elif obj[9] == 'tue':
									return 'no'
								elif obj[9] == 'fri':
									return 'no'
								elif obj[9] == 'thu':
									return 'no'
								else: return 'no'
							elif obj[2] == 'divorced':
								return 'yes'
							elif obj[2] == 'single':
								return 'no'
							else: return 'no'
						elif obj[3] == 'basic.6y':
							# {"feature": "default", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[4] == 'unknown':
								return 'no'
							elif obj[4] == 'no':
								# {"feature": "euribor3m", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[18]>4.857:
									return 'yes'
								elif obj[18]<=4.857:
									return 'no'
								else: return 'no'
							else: return 'yes'
						elif obj[3] == 'unknown':
							# {"feature": "default", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[4] == 'no':
								return 'no'
							elif obj[4] == 'unknown':
								return 'yes'
							else: return 'yes'
						elif obj[3] == 'high.school':
							return 'yes'
						elif obj[3] == 'professional.course':
							# {"feature": "day_of_week", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[9] == 'fri':
								return 'no'
							elif obj[9] == 'thu':
								return 'yes'
							else: return 'yes'
						elif obj[3] == 'university.degree':
							return 'yes'
						else: return 'yes'
					elif obj[1] == 'admin.':
						# {"feature": "education", "instances": 28, "metric_value": 0.9852, "depth": 6}
						if obj[3] == 'university.degree':
							# {"feature": "default", "instances": 14, "metric_value": 1.0, "depth": 7}
							if obj[4] == 'no':
								# {"feature": "marital", "instances": 12, "metric_value": 0.9799, "depth": 8}
								if obj[2] == 'married':
									# {"feature": "euribor3m", "instances": 7, "metric_value": 0.5917, "depth": 9}
									if obj[18]<=4.859:
										return 'no'
									elif obj[18]>4.859:
										return 'yes'
									else: return 'yes'
								elif obj[2] == 'single':
									# {"feature": "housing", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[5] == 'no':
										return 'yes'
									elif obj[5] == 'yes':
										return 'no'
									else: return 'no'
								elif obj[2] == 'divorced':
									return 'yes'
								else: return 'yes'
							elif obj[4] == 'unknown':
								return 'yes'
							else: return 'yes'
						elif obj[3] == 'high.school':
							# {"feature": "euribor3m", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[18]<=4.856:
								# {"feature": "housing", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[5] == 'yes':
									return 'no'
								elif obj[5] == 'no':
									# {"feature": "marital", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[2] == 'married':
										return 'yes'
									elif obj[2] == 'single':
										return 'no'
									else: return 'no'
								else: return 'yes'
							elif obj[18]>4.856:
								# {"feature": "day_of_week", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[9] == 'wed':
									return 'yes'
								elif obj[9] == 'fri':
									return 'yes'
								elif obj[9] == 'thu':
									return 'no'
								else: return 'no'
							else: return 'yes'
						elif obj[3] == 'basic.9y':
							return 'no'
						elif obj[3] == 'basic.4y':
							# {"feature": "marital", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2] == 'married':
								return 'yes'
							elif obj[2] == 'single':
								return 'no'
							else: return 'no'
						elif obj[3] == 'basic.6y':
							return 'no'
						else: return 'no'
					elif obj[1] == 'services':
						# {"feature": "default", "instances": 22, "metric_value": 0.976, "depth": 6}
						if obj[4] == 'no':
							# {"feature": "euribor3m", "instances": 12, "metric_value": 0.8113, "depth": 7}
							if obj[18]<=4.856:
								# {"feature": "education", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[3] == 'high.school':
									# {"feature": "marital", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[2] == 'married':
										return 'no'
									elif obj[2] == 'divorced':
										# {"feature": "housing", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == 'yes':
											# {"feature": "contact", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7] == 'telephone':
												# {"feature": "month", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == 'may':
													# {"feature": "day_of_week", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'thu':
														# {"feature": "pdays", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=5191:
																					return 'yes'
																				else: return 'yes'
																			else: return 'yes'
																		else: return 'yes'
																	else: return 'yes'
																else: return 'yes'
															else: return 'yes'
														else: return 'yes'
													else: return 'yes'
												else: return 'yes'
											else: return 'yes'
										else: return 'yes'
									else: return 'yes'
								elif obj[3] == 'basic.6y':
									return 'yes'
								elif obj[3] == 'basic.4y':
									return 'yes'
								elif obj[3] == 'professional.course':
									return 'yes'
								else: return 'yes'
							elif obj[18]>4.856:
								return 'yes'
							else: return 'yes'
						elif obj[4] == 'unknown':
							# {"feature": "marital", "instances": 10, "metric_value": 0.971, "depth": 7}
							if obj[2] == 'married':
								# {"feature": "euribor3m", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[18]<=4.857:
									# {"feature": "education", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[3] == 'high.school':
										# {"feature": "housing", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[5] == 'yes':
											# {"feature": "day_of_week", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[9] == 'tue':
												return 'yes'
											elif obj[9] == 'mon':
												return 'no'
											else: return 'no'
										elif obj[5] == 'no':
											return 'no'
										else: return 'no'
									elif obj[3] == 'basic.6y':
										return 'yes'
									else: return 'yes'
								elif obj[18]>4.857:
									# {"feature": "education", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[3] == 'high.school':
										return 'yes'
									elif obj[3] == 'basic.6y':
										return 'no'
									else: return 'no'
								else: return 'yes'
							elif obj[2] == 'divorced':
								return 'no'
							elif obj[2] == 'single':
								return 'no'
							else: return 'no'
						else: return 'no'
					elif obj[1] == 'technician':
						# {"feature": "euribor3m", "instances": 19, "metric_value": 0.998, "depth": 6}
						if obj[18]>4.855:
							# {"feature": "day_of_week", "instances": 18, "metric_value": 0.9911, "depth": 7}
							if obj[9] == 'wed':
								# {"feature": "education", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[3] == 'university.degree':
									# {"feature": "marital", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[2] == 'married':
										return 'no'
									elif obj[2] == 'single':
										return 'yes'
									else: return 'yes'
								elif obj[3] == 'professional.course':
									# {"feature": "default", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[4] == 'unknown':
										return 'no'
									elif obj[4] == 'no':
										return 'yes'
									else: return 'yes'
								elif obj[3] == 'high.school':
									# {"feature": "housing", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[5] == 'yes':
										return 'yes'
									elif obj[5] == 'no':
										return 'no'
									else: return 'no'
								elif obj[3] == 'basic.9y':
									return 'yes'
								else: return 'yes'
							elif obj[9] == 'tue':
								# {"feature": "marital", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2] == 'married':
									# {"feature": "education", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3] == 'professional.course':
										# {"feature": "default", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[4] == 'no':
											# {"feature": "housing", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5] == 'no':
												# {"feature": "contact", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=5191:
																					return 'yes'
																				else: return 'yes'
																			else: return 'yes'
																		else: return 'yes'
																	else: return 'yes'
																else: return 'yes'
															else: return 'yes'
														else: return 'yes'
													else: return 'yes'
												else: return 'yes'
											else: return 'yes'
										else: return 'yes'
									else: return 'yes'
								elif obj[2] == 'single':
									return 'yes'
								else: return 'yes'
							elif obj[9] == 'fri':
								# {"feature": "education", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[3] == 'basic.9y':
									return 'no'
								elif obj[3] == 'university.degree':
									return 'no'
								elif obj[3] == 'basic.6y':
									return 'yes'
								else: return 'yes'
							elif obj[9] == 'mon':
								return 'no'
							elif obj[9] == 'thu':
								return 'yes'
							else: return 'yes'
						elif obj[18]<=4.855:
							return 'yes'
						else: return 'yes'
					elif obj[1] == 'management':
						# {"feature": "euribor3m", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[18]<=4.8580000000000005:
							# {"feature": "marital", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[2] == 'married':
								# {"feature": "education", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[3] == 'university.degree':
									# {"feature": "day_of_week", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[9] == 'tue':
										# {"feature": "default", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[4] == 'no':
											# {"feature": "housing", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5] == 'no':
												# {"feature": "contact", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=5191:
																					return 'yes'
																				else: return 'yes'
																			else: return 'yes'
																		else: return 'yes'
																	else: return 'yes'
																else: return 'yes'
															else: return 'yes'
														else: return 'yes'
													else: return 'yes'
												else: return 'yes'
											else: return 'yes'
										else: return 'yes'
									elif obj[9] == 'thu':
										return 'no'
									else: return 'no'
								elif obj[3] == 'basic.4y':
									# {"feature": "housing", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[5] == 'yes':
										return 'no'
									elif obj[5] == 'no':
										return 'yes'
									else: return 'yes'
								elif obj[3] == 'basic.9y':
									return 'yes'
								elif obj[3] == 'basic.6y':
									return 'no'
								else: return 'no'
							elif obj[2] == 'divorced':
								return 'no'
							else: return 'no'
						elif obj[18]>4.8580000000000005:
							return 'yes'
						else: return 'yes'
					elif obj[1] == 'entrepreneur':
						# {"feature": "marital", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[2] == 'married':
							return 'yes'
						elif obj[2] == 'divorced':
							# {"feature": "education", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3] == 'high.school':
								return 'yes'
							elif obj[3] == 'university.degree':
								return 'no'
							else: return 'no'
						else: return 'yes'
					elif obj[1] == 'retired':
						# {"feature": "default", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[4] == 'unknown':
							# {"feature": "housing", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5] == 'no':
								return 'yes'
							elif obj[5] == 'yes':
								return 'no'
							else: return 'no'
						elif obj[4] == 'no':
							return 'no'
						else: return 'no'
					elif obj[1] == 'housemaid':
						# {"feature": "marital", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[2] == 'married':
							# {"feature": "education", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[3] == 'basic.4y':
								return 'no'
							elif obj[3] == 'high.school':
								return 'yes'
							elif obj[3] == 'basic.9y':
								return 'yes'
							elif obj[3] == 'professional.course':
								return 'yes'
							else: return 'yes'
						elif obj[2] == 'single':
							return 'no'
						else: return 'no'
					elif obj[1] == 'unemployed':
						# {"feature": "marital", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[2] == 'married':
							return 'no'
						elif obj[2] == 'divorced':
							return 'yes'
						else: return 'yes'
					elif obj[1] == 'self-employed':
						return 'no'
					elif obj[1] == 'unknown':
						return 'no'
					elif obj[1] == 'student':
						return 'no'
					else: return 'no'
				elif obj[0]<=24.002621701278:
					return 'no'
				else: return 'no'
			elif obj[6] == 'yes':
				# {"feature": "age", "instances": 33, "metric_value": 0.9673, "depth": 4}
				if obj[0]>22:
					# {"feature": "education", "instances": 32, "metric_value": 0.9745, "depth": 5}
					if obj[3] == 'high.school':
						# {"feature": "marital", "instances": 8, "metric_value": 1.0, "depth": 6}
						if obj[2] == 'married':
							return 'no'
						elif obj[2] == 'single':
							return 'yes'
						elif obj[2] == 'divorced':
							return 'yes'
						else: return 'yes'
					elif obj[3] == 'basic.6y':
						# {"feature": "euribor3m", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[18]<=4.8580000000000005:
							return 'yes'
						elif obj[18]>4.8580000000000005:
							return 'no'
						else: return 'no'
					elif obj[3] == 'university.degree':
						return 'yes'
					elif obj[3] == 'basic.4y':
						# {"feature": "job", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[1] == 'blue-collar':
							return 'no'
						elif obj[1] == 'housemaid':
							return 'yes'
						else: return 'yes'
					elif obj[3] == 'unknown':
						return 'yes'
					elif obj[3] == 'basic.9y':
						# {"feature": "housing", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5] == 'yes':
							return 'no'
						elif obj[5] == 'no':
							return 'yes'
						else: return 'yes'
					elif obj[3] == 'professional.course':
						# {"feature": "job", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1] == 'admin.':
							return 'yes'
						elif obj[1] == 'blue-collar':
							return 'no'
						else: return 'no'
					else: return 'yes'
				elif obj[0]<=22:
					return 'yes'
				else: return 'yes'
			elif obj[6] == 'unknown':
				return 'no'
			else: return 'no'
		elif obj[11]>6:
			return 'no'
		else: return 'no'
	else: return 'no'
