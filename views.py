from mysql.connector import (connection)
from mysql.connector import errorcode, errors, Error
from flask_restful import Resource

class table_test(Resource):
    def get(self):
        print >> sys.stderr, "Execution started"
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = cnx.cursor(dictionary=True)
            #cursor.execute("SELECT * from animal_table")
            cursor.execute("""SELECT a.Animal_ID,animalname,animaltype,eartag,eid,p.pasturenumber, weight,
                                    height,gender,sex,breed,status,current_expt_no,Herd,breeder,currentframescore,
                                    damframescore,comments,species,a.email_id,brand,brandlocation,tattooleft,tattooright, 
                                    alternativeid,registration,color,hornstatus,dam,sire,DOB,howacquired,dateacquired,
                                    howdisposed,datedisposed ,disposalreason ,herdnumberlocation ,herdstatus ,
                                    howconceived, managementcode ,ownerID ,springfall ,includeinlookups from animal_table a,pasture p WHERE a.pasture_ID=p.pasture_ID""")
            rows = cursor.fetchall()
            print("Fetch Test Completed")
            cursor.close()

            cnx.close()

        return jsonify(rows)


    def update(self):
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            # New comment line
            cursor = cnx.cursor(dictionary=True)

            update_users = ("""UPDATE login SET first_name=%(first_name)s, last_name=%(last_name)s, 
                                pswd_hash=%(pswd_hash)s, email_id=%(email_id)s, roles=%(roles)s, registered_at=%(registered_at)s
                                WHERE Server=%s(email_id, first_name, last_name, pswd_hash, roles, registered_at)""")
            print >> sys.stderr, "Initialized"
            data = request.get_json(force=True)
            print >> sys.stderr, "Got the data"
            for k, v in data.iteritems():
                print >> sys.stderr, ("Code : {0} ==> Value : {1}".format(k, v))
            print>>sys.stderr, "Next is the execute command, Here it goes"
            try:
                cursor.execute(update_users, data)
                cnx.commit()
                return "Success", 201
            except AttributeError:
                raise errors.OperationalError("MySQL Connection not available.")
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return None
            finally:
                cursor.close()
                cnx.close()


class TableAnimalUpdate(Resource):
    def get(self, Animal_ID):
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("""SELECT * FROM animal_table WHERE Animal_ID = %s""", (Animal_ID,))
            rows = cursor.fetchall()
            print("Fetch Completed")
            print(rows)
            cursor.close()
            cnx.close()
            return jsonify(rows)

    def patch(self,Animal_ID):

        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            data = request.get_json(force=True)
            print(data)
            for k, v in data.iteritems():
                print >> sys.stderr, ("Code : {0} ==> Value : {1}".format(k, v))
            cursor = cnx.cursor(dictionary=True)
            print("animal update++++")
            update_animaldata = ("""UPDATE animal_table SET animalname=%(animalname)s,animaltype=%(animaltype)s,eartag=%(eartag)s,eid=%(eid)s,pasture_ID=%(pasture_ID)s, weight=%(weight)s,
                                                height=%(height)s,gender=%(gender)s,sex=%(sex)s,breed=%(breed)s,status=%(status)s,current_expt_no=%(current_expt_no)s,Herd=%(Herd)s,breeder=%(breeder)s,currentframescore=%(currentframescore)s,
                                                damframescore=%(damframescore)s,comments=%(comments)s,species=%(species)s,email_id=%(email_id)s,brand=%(brand)s,brandlocation=%(brandlocation)s,tattooleft=%(tattooleft)s,tattooright=%(tattooright)s, 
                                                alternativeid=%(alternativeid)s,registration=%(registration)s,color=%(color)s,hornstatus=%(hornstatus)s,dam=%(dam)s,sire=%(sire)s,DOB=%(DOB)s,howacquired=%(howacquired)s,dateacquired=%(dateacquired)s,
                                                howdisposed=%(howdisposed)s,datedisposed=%(datedisposed)s ,disposalreason=%(disposalreason)s ,herdnumberlocation=%(herdnumberlocation)s ,herdstatus=%(herdstatus)s ,
                                                howconceived=%(howconceived)s, managementcode=%(managementcode)s ,ownerID=%(ownerID)s ,springfall=%(springfall)s ,includeinlookups=%(includeinlookups)s
                                                WHERE Animal_ID=%(Animal_ID)s""")
            try:
                cursor.execute(update_animaldata,data)
                print("here after execute in update animal ")
                cnx.commit()
                return "Success", 201
            finally:
                cursor.close()
                cnx.close()

    def delete(self,Animal_ID):
        #data = request.get_json(force=True)
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = cnx.cursor(dictionary=True)
            print("animal delete++++")
            update_animaldata = "DELETE FROM animal_table WHERE Animal_ID = %s"
            try:
                cursor.execute(update_animaldata,(Animal_ID,))
                print("here after execute in delete animal ")
                cnx.commit()
                return "Success", 201
            except AttributeError:
                raise errors.OperationalError("MySQL Connection not available.")
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return None
            finally:
                cursor.close()
                cnx.close()


class TableAnimalAdd(Resource):
    def get(self, Animal_ID):
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("""SELECT animalname,Animal_ID FROM animal_table WHERE Animal_ID = %s""", (Animal_ID,))
            rows = cursor.fetchall()
            print("Fetch Completed")
            print(rows)
            cursor.close()
            cnx.close()
            return jsonify(rows)

    def post(self):
        data=request.get_json(force=True)
        print(data)
        for k, v in data.iteritems():
            print >> sys.stderr, ("Code : {0} ==> Value : {1}".format(k, v))
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = cnx.cursor(dictionary=True)
            print("here in add animal class from the API call")
            insert_animaldata = ("""INSERT INTO animal_table (animalname,animaltype,eartag,eid,pasture_ID, weight,
                                    height,gender,sex,breed,status,current_expt_no,Herd,breeder,currentframescore,
                                    damframescore,comments,species,email_id,brand,brandlocation,tattooleft,tattooright, 
                                    alternativeid,registration,color,hornstatus,dam,sire,DOB,howacquired,dateacquired,
                                    howdisposed,datedisposed ,disposalreason ,herdnumberlocation ,herdstatus ,
                                    howconceived, managementcode ,ownerID ,springfall ,includeinlookups) 
                                    VALUES ( %(animalname)s, %(animaltype)s, %(eartag)s, %(eid)s, %(pasture_ID)s, 
                                    %(weight)s, %(height)s, %(gender)s, %(sex)s, %(breed)s, %(status)s, 
                                    %(current_expt_no)s, %(Herd)s,%(breeder)s, %(currentframescore)s, %(damframescore)s,
                                    %(comments)s,%(species)s, %(email_id)s,%(brand)s, %(brandlocation)s, %(tattooleft)s,
                                    %(tattooright)s, %(alternativeid)s, %(registration)s, %(color)s, %(hornstatus)s,
                                    %(dam)s, %(sire)s, %(DOB)s, %(howacquired)s,%(dateacquired)s, %(howdisposed)s,
                                    %(datedisposed)s, %(disposalreason)s,%(herdnumberlocation)s, %(herdstatus)s, 
                                    %(howconceived)s, %(managementcode)s,%(ownerID)s, %(springfall)s,
                                    %(includeinlookups)s)""")
            try:
                cursor.execute(insert_animaldata, data)
                print("here after execute")
                cnx.commit()
                return "Success", 201
            except AttributeError:
                raise errors.OperationalError("MySQL Connection not available.")
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return None
            finally:
                cursor.close()
                cnx.close()

    def patch(self,Animal_ID):

        print >> sys.stderr, "Execution started in Repro"
        print >> sys.stderr, "{}".format(Animal_ID)
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                return err
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                return err
            else:
                print(err)
                return err
        else:
            cursor = cnx.cursor(dictionary=True)
            animal_data=("""SELECT a.animalname,ID,r.Animal_id, breeding, pregnancy, calfdob,damageatbirth,
                                    siblingcode, calfatside, totalcalves, previouscalf, currentcalf,calfbirthweight,
                                    calfsex, r.email_id, pasturenumber, damcalvingdisposition, calvingease,udderscore,
                                    conditionscorecalving,hiphtweaning,hiphtbreeding,damdisposition,cowframescore,cowwtbreeding,
                                    cowhtbreeding,cowwtweaning,cowhtweaning,cowwtcalving,cowhtcalving,bcsweaning,bcscalving,bcsbreeding,
                                    customcowwt,customcowht,bulldisposition,bullframescore,bullwtprebreeding,bullhtprebreeding,
                                    fertility,mobility,conc,deadabnormal,date from reproduction r,animal_table a where a.Animal_ID=r.Animal_id and r.Animal_id=%s""")
            cursor.execute(animal_data,(Animal_ID,))
            rows = cursor.fetchall()
            print("Fetch Completed")
            cursor.close()

            cnx.close()

        return jsonify(rows)


class TableInventoryPastureHistory(Resource):
    def get(self):
        print >> sys.stderr, "Execution started"
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                return err
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                return err
            else:
                print(err)
                return err
        else:
            cursor = cnx.cursor(dictionary=True)
            #cursor.execute("SELECT * from pasture_history")
            cursor.execute("""SELECT fertilizer_name , event_date, qualityofburn, 
                                    fertilizer_applicationrate, chemicalname, applicationrate, pesticide_method, 
                                    email_ID, pasturenumber, comments, fertilizer_method from pasture_history """)
            rows = cursor.fetchall()
            print rows
            print("Fetch Completed")
            cursor.close()

            cnx.close()

        return jsonify(rows)

    def post(self):
        data=request.get_json(force=True)
        print(data)
        for k, v in data.iteritems():
            print >> sys.stderr, ("Code : {0} ==> Value : {1}".format(k, v))
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = cnx.cursor(dictionary=True)
            print("here in pasture class from the API call")
            insert_animaldata = ("""INSERT INTO pasture_history (fertilizer_name , event_date, qualityofburn, 
                                    fertilizer_applicationrate, chemicalname, applicationrate, pesticide_method, 
                                    pasture_ID, email_ID, pasturenumber, comments, fertilizer_method) 
                                    VALUES( %(fertilizer_name)s,%(event_date)s,%(qualityofburn)s, 
                                    %(fertilizer_applicationrate)s, %(chemicalname)s,%(applicationrate)s,
                                    %(pesticide_method)s, %(pasture_ID)s,%(email_id)s,%(pasturenumber)s, 
                                    %(comments)s,%(fertilizer_method)s )""")
            try:
                cursor.execute(insert_animaldata, data)
                print("here after execute in pasture")
                cnx.commit()
                return "Success", 201
            except AttributeError:
                raise errors.OperationalError("MySQL Connection not available.")
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return None
            finally:
                cursor.close()
                cnx.close()

    def patch(self):
        print("in pasture patch")
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            data = request.get_json(force=True)
            print(data)
            for k, v in data.iteritems():
                print >> sys.stderr, ("Code : {0} ==> Value : {1}".format(k, v))
            cursor = cnx.cursor(dictionary=True)
            print("pasture update++++")
            update_animaldata = ("""UPDATE pasture_history SET fertilizer_name=%(fertilizer_name)s,
                                                event_date=%(event_date)s,qualityofburn=%(qualityofburn)s,
                                                fertilizer_applicationrate=%(fertilizer_applicationrate)s,
                                                chemicalname=%(chemicalname)s, applicationrate=%(applicationrate)s,
                                                fertilizer_method=%(fertilizer_method)s, pasture_ID =%(pasture_ID)s,
                                                email_ID=%(email_ID)s,pasturenumber=%(pasturenumber)s,
                                                comments=%(comments)s,pesticide_method=%(pesticide_method)s
                                                WHERE pasturenumber =%(pasturenumber)s and event_date=%(event_date)s""")
            try:
                cursor.execute(update_animaldata,data)
                print("here after execute in update pasture ")
                cnx.commit()
                return "Success", 201
            except ValueError, e:
                print(e)
                return None
            finally:
                cursor.close()
                cnx.close()

    def delete(self, pasture_ID,event_date):
        # data = request.get_json(force=True)
        print("delete method++")
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = cnx.cursor(dictionary=True)
            print("animal delete++++")
            update_animaldata = "DELETE FROM pasture_history WHERE pasturenumber = %s and event_date=%s"
            try:
                cursor.execute(update_animaldata, (pasture_ID, event_date,))
                print("here after execute in delete pasture ")
                cnx.commit()
                return "Success", 201
            except AttributeError:
                raise errors.OperationalError("MySQL Connection not available.")
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return None
            finally:
                cursor.close()
                cnx.close()


class TableInventoryPasture(Resource):
    def get(self):
        print >> sys.stderr, "Execution started in pasture"
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                return err
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                return err
            else:
                print(err)
                return err
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * from pasture")
            rows = cursor.fetchall()
            print("Fetch Completed")
            cursor.close()

            cnx.close()

        return jsonify(rows)


class TableInventoryFormulary(Resource):
    def get(self):
        print >> sys.stderr, "Execution started"
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT Medicine_ID,date,drug,vial_size,Lot_no,expirydate,location,roa,purchasedate,total_quantity,qty_in_stock,email_id from formulary order by drug")
            rows = cursor.fetchall()
            print("Fetch Completed")
            cursor.close()

            cnx.close()
        return jsonify(rows)

    def post(self):
        data=request.get_json(force=True)
        print(data)
        for k, v in data.iteritems():
            print >> sys.stderr, ("Code : {0} ==> Value : {1}".format(k, v))
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = cnx.cursor(dictionary=True)
            print("here in formulary class from the API call")
            insert_animaldata = ("""INSERT INTO formulary (date,drug,vial_size,Lot_no,expirydate,location,roa,
                                    purchasedate,total_quantity,email_id,qty_in_stock)  VALUES( %(date)s,%(drug)s,%(vial_size)s, 
                                    %(Lot_no)s, %(expirydate)s,%(location)s,%(roa)s, %(purchasedate)s,%(total_quantity)s,%(email_id)s,%(qty_in_stock)s )""")
            try:
                cursor.execute(insert_animaldata, data)
                print("here after execute in formulary")
                cnx.commit()
                return "Success", 201
            except AttributeError:
                raise errors.OperationalError("MySQL Connection not available.")
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return None
            finally:
                cursor.close()
                cnx.close()

    def patch(self):
        print("in formulary patch")
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            data = request.get_json(force=True)
            print(data)
            for k, v in data.iteritems():
                print >> sys.stderr, ("Code : {0} ==> Value : {1}".format(k, v))
            cursor = cnx.cursor(dictionary=True)
            print("formulary update++++")
            update_animaldata = ("""UPDATE formulary SET
                                                date=%(date)s,vial_size=%(vial_size)s,
                                                drug=%(drug)s,Lot_no =%(Lot_no)s,
                                                expirydate=%(expirydate)s, location=%(location)s,
                                                purchasedate=%(purchasedate)s, roa =%(roa)s,
                                                email_ID=%(email_ID)s,total_quantity=%(total_quantity)s
                                                WHERE  Medicine_ID=%(Medicine_ID)s""")
            try:
                cursor.execute(update_animaldata,data)
                print("here after execute in update pasture ")
                cnx.commit()
                return "Success", 201
            finally:
                cursor.close()
                cnx.close()

    def delete(self,Medicine_ID):
        # data = request.get_json(force=True)
        print("delete method++")
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = cnx.cursor(dictionary=True)
            print("formulary delete++++")
            update_animaldata = "DELETE FROM formulary WHERE Medicine_ID=%s"
            try:
                cursor.execute(update_animaldata, (Medicine_ID,))
                print("here after execute in delete formulary ")
                cnx.commit()
                return "Success", 201
            except AttributeError:
                raise errors.OperationalError("MySQL Connection not available.")
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return None
            finally:
                cursor.close()
                cnx.close()


class TableHealthList(Resource):
    def get(self):
        print >> sys.stderr, "Execution started"
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT result,Record_ID,Animal_id,create_date,email_id,medical_notes,location,Amt_given,route,water_feed,"
                           "withdraw_time,(select drug from formulary where medical_record.Medicine_ID=formulary.Medicine_ID)drug "
                           "from medical_record;")
            rows = cursor.fetchall()
            print("Fetch Completed")
            cursor.close()

            cnx.close()

        return jsonify(rows)

    def patch(self):
        print("in health patch")
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            data = request.get_json(force=True)
            print(data)
            for k, v in data.iteritems():
                print >> sys.stderr, ("Code : {0} ==> Value : {1}".format(k, v))
            cursor = cnx.cursor(dictionary=True)
            print("health update++++")
            update_animaldata = ("""UPDATE medical_record SET Animal_id=%(Animal_id)s,
                                                create_date=%(create_date)s,Medicine_ID=%(Medicine_ID)s,
                                                medical_notes=%(medical_notes)s,result=%(result)s,
                                                location=%(location)s, Amt_given=%(Amt_given)s,
                                                route=%(route)s, water_feed =%(water_feed)s,
                                                email_ID=%(email_ID)s,withdraw_time=%(withdraw_time)s
                                                WHERE Record_ID =%(Record_ID)s""")
            update_formulary = ( """UPDATE formulary SET qty_in_stock=qty_in_stock-%(difference)s where Medicine_ID=%(Medicine_ID)s""")
            try:
                cursor.execute(update_animaldata,data)
                cursor.execute(update_formulary, data)
                print("here after execute in update health ")
                cnx.commit()
                return "Success", 201
            finally:
                cursor.close()
                cnx.close()

    def delete(self,Record_ID):
        # data = request.get_json(force=True)
        print("delete method++")
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = cnx.cursor(dictionary=True)
            print("health record delete++++")
            update_animaldata = "DELETE FROM medical_record WHERE Record_ID = %s"
            try:
                cursor.execute(update_animaldata, (Record_ID,))
                print("here after execute in delete health record ")
                cnx.commit()
                return "Success", 201
            except AttributeError:
                raise errors.OperationalError("MySQL Connection not available.")
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return None
            finally:
                cursor.close()
                cnx.close()


class TableHerdUniqueName(Resource):
    def get(self):
        print >> sys.stderr, "Execution started in herd unique name"
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                return err
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                return err
            else:
                print(err)
                return err
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("select distinct name from herds")
            rows = cursor.fetchall()
            print("Fetch Completed")
            cursor.close()

            cnx.close()

        return jsonify(rows)

    def post(self,name):
        print(name)
        print >> sys.stderr, "Execution started in herd unique name"
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                return err
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                return err
            else:
                print(err)
                return err
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("select * from herds where name=%s",(name,))
            rows = cursor.fetchall()
            print("Fetch Completed")
            cursor.close()

            cnx.close()

        return jsonify(rows)

    def patch(self):
        data = request.get_json(force=True)
        print(data)
        for k, v in data.iteritems():
            print >> sys.stderr, ("Code : {0} ==> Value : {1}".format(k, v))
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = cnx.cursor(dictionary=True)
            print("here in herd name  from the API call")
            insert_animaldata = ("""UPDATE herds SET string=%(string)s where name=%(name)s""")
            try:
                cursor.execute(insert_animaldata, data)
                print("here after execute")
                cnx.commit()
                return "Success", 201
            except AttributeError:
                raise errors.OperationalError("MySQL Connection not available.")
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return None
            finally:
                cursor.close()
                cnx.close()


class TableHerd(Resource):
    def get(self):
        print >> sys.stderr, "Execution started"
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                return err
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                return err
            else:
                print(err)
                return err
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("select * from herds")
            #cursor.execute("select distinct name,description,create_date from herd")
            rows = cursor.fetchall()
            print("Fetch Completed")
            cursor.close()

            cnx.close()

        return jsonify(rows)

    def patch(self):
        data = request.get_json(force=True)
        print(data)
        print name;
        print create_date;
        for k, v in data.iteritems():
            print >> sys.stderr, ("Code : {0} ==> Value : {1}".format(k, v))
        print >> sys.stderr, "Execution started in herds"
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                return err
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                return err
            else:
                print(err)
                return err
        else:
            cursor = cnx.cursor(dictionary=True)
            update_data=("""UPDATE herds SET AID_string=%(AID_string)s, description=%(description)s, name=%(name)s, 
                                     create_date=%(create_date)s where name=%(name)s and create_date=%(create_date)s""")
            #cursor.execute(update_data,data)
            try:
                cursor.execute(update_data,data)
                print("here after execute")
                cnx.commit()
                return "Success", 201
            except AttributeError:
                raise errors.OperationalError("Operational error.")
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return None
            finally:
                cursor.close()
                cnx.close()

    def post(self):
        data = request.get_json(force=True)
        print(data)
        for k, v in data.iteritems():
            print >> sys.stderr, ("Code : {0} ==> Value : {1}".format(k, v))
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = cnx.cursor(dictionary=True)
            print("here in herd from the API call")
            insert_animaldata = ("""INSERT INTO herds (create_date,name,description,AID_string) 
                                    VALUES ( %(create_date)s, %(name)s, %(description)s, %(AID_string)s)""")
            try:
                cursor.execute(insert_animaldata, data)
                print("here after execute")
                cnx.commit()
                return "Success", 201
            except AttributeError:
                raise errors.OperationalError("MySQL Connection not available.")
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return None
            finally:
                cursor.close()
                cnx.close()

    def delete(self):
        data = request.get_json(force=True)
        print("delete method++")
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = cnx.cursor(dictionary=True)
            print("herd delete++++")
            update_animaldata = "DELETE FROM herds WHERE name = %(name)s and create_date=%(create_date)s"
            try:
                cursor.execute(update_animaldata,data)
                print("here after execute in delete herds ")
                cnx.commit()
                return "Success", 201
            except AttributeError:
                raise errors.OperationalError("MySQL Connection not available.")
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return None
            finally:
                cursor.close()
                cnx.close()


class TableExperiment(Resource):
    def get(self,Animal_ID):
        print >> sys.stderr, "Execution started"
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                return err
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                return err
            else:
                print(err)
                return err
        else:
            cursor = cnx.cursor(dictionary=True)
            # cursor.execute("select * from herd")
            cursor.execute("""select a.animalname,e.animaltype,e.birthweight,e.birthweightadj,e.sireframescore,e.bcsrecent,e.bcsprevious,e.bcsdifference,
                                    e.damwtatwean,e.weanheight,e.weanweight,e.weandate,e.weangpd,e.weanwda,e.weanweightdate,e.adj205w,e.adj205h,e.weanframescore,e.ageatwean,
                                    e.yearlingweight,e.yearlingheight,e.yearlingdate,e.adjyearlingw,e.adjyearlingh,e.yearlingframescore,e.ageatyearling,e.customweight,
                                    e.customweightdate,e.customheight,e.customheightdate,e.currentwtcow,e.adj365dht,e.currentwtheifer,e.backfat,e.treatment,e.blockpen,
                                    e.replicate,e.email_id,e.Animal_ID,e.expt_date,e.expt_name from animal_table a,experiments e where a.Animal_ID=e.Animal_ID and e.Animal_ID=%s order by expt_date desc""",(Animal_ID,))
            rows = cursor.fetchall()
            print("Fetch Completed")
            cursor.close()

            cnx.close()

        return jsonify(rows)
    def post(self):
        data=request.get_json(force=True)
        print(data)
        for k, v in data.iteritems():
           print >> sys.stderr, ("Code : {0} ==> Value : {1}".format(k, v))
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = cnx.cursor(dictionary=True)
            print("here in pasture class from the API call")
            insert_animaldata = ("""INSERT INTO experiments (animaltype,birthweight,birthweightadj,sireframescore,bcsrecent,bcsprevious,bcsdifference,
                                    damwtatwean,weanheight,weanweight,weandate,weangpd,weanwda,weanweightdate,adj205w,adj205h,weanframescore,ageatwean,
                                    yearlingweight,yearlingheight,yearlingdate,adjyearlingw,adjyearlingh,yearlingframescore,ageatyearling,customweight,
                                    customweightdate,customheight,customheightdate,currentwtcow,adj365dht,currentwtheifer,backfat,treatment,blockpen,
                                    replicate,email_id,Animal_ID,expt_date) 
                                    VALUES( %(animaltype)s,%(birthweight)s,%(birthweightadj)s, %(sireframescore)s, %(bcsrecent)s,%(bcsprevious)s,%(bcsdifference)s,
                                    %(damwtatwean)s, %(weanheight)s,%(weanweight)s ,%(weandate)s,%(weangpd)s,%(weanwda)s,%(weanweightdate)s,%(adj205w)s,%(adj205h)s,%(weanframescore)s,%(ageatwean)s,
                                    %(yearlingweight)s,%(yearlingheight)s,%(yearlingdate)s,%(adjyearlingw)s,%(adjyearlingh)s,%(yearlingframescore)s,%(ageatyearling)s,%(customweight)s,
                                    %(customweightdate)s,%(customheight)s,%(customheightdate)s,%(currentwtcow)s,%(adj365dht)s,%(currentwtheifer)s,%(backfat)s,
                                    %(treatment)s,%(blockpen)s,%(replicate)s,%(email_id)s,%(Animal_ID)s,%(expt_date)s)""")
            try:
                cursor.execute(insert_animaldata, data)
                print("here after insert execute in experiment")
                cnx.commit()
                return "Success", 201
            except AttributeError:
                raise errors.OperationalError("MySQL Connection not available.")
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return err
            finally:
                cursor.close()
                cnx.close()

    def patch(self):
        print("in experiment patch")
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            data = request.get_json(force=True)
            print(data)
            for k, v in data.iteritems():
                print >> sys.stderr, ("Code : {0} ==> Value : {1}".format(k, v))
            cursor = cnx.cursor(dictionary=True)
            print("experiment update++++")
            update_animaldata = ("""UPDATE experiments SET animaltype=%(animaltype)s,
                                                birthweight=%(birthweight)s,birthweightadj=%(birthweightadj)s,
                                                sireframescore=%(sireframescore)s,
                                                bcsrecent=%(bcsrecent)s, bcsprevious=%(bcsprevious)s,
                                                bcsdifference=%(bcsdifference)s, damwtatwean =%(damwtatwean)s,
                                                email_ID=%(email_ID)s,weanheight=%(weanheight)s,
                                                weanweight=%(weanweight)s,weandate=%(weandate)s,weangpd=%(weangpd)s,weanwda=%(weanwda)s,
                                                weanweightdate=%(weanweightdate)s,adj205w=%(adj205w)s,adj205h=%(adj205h)s,weanframescore=%(weanframescore)s,
                                                ageatwean=%(ageatwean)s,yearlingweight=%(yearlingweight)s,yearlingheight=%(yearlingheight)s,yearlingdate=%(yearlingdate)s,
                                                adjyearlingw=%(adjyearlingw)s,adjyearlingh=%(adjyearlingh)s,yearlingframescore=%(yearlingframescore)s,ageatyearling=%(ageatyearling)s,
                                                customweight=%(customweight)s,customweightdate=%(customweightdate)s,customheight=%(customheight)s,customheightdate=%(customheightdate)s,
                                                currentwtcow=%(currentwtcow)s,adj365dht=%(adj365dht)s,currentwtheifer=%(currentwtheifer)s,backfat=%(backfat)s,treatment=%(treatment)s,
                                                blockpen=%(blockpen)s,replicate=%(replicate)s,Animal_ID=%(Animal_ID)s,expt_date=%(expt_date)s,expt_name=%(expt_name)s
                                                WHERE Animal_ID =%(Animal_ID)s and expt_date=%(expt_date)s""")
            try:
                cursor.execute(update_animaldata,data)
                print("here after execute in update experiment ")
                cnx.commit()
                return "Success", 201
            finally:
                cursor.close()
                cnx.close()

    def delete(self, Animal_ID,expt_date):
        # data = request.get_json(force=True)
        print("delete method++")
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = cnx.cursor(dictionary=True)
            print("animal delete++++")
            update_animaldata = "DELETE FROM experiment WHERE Animal_ID = %s and expt_date=%s"
            try:
                cursor.execute(update_animaldata, (Animal_ID, expt_date,))
                print("here after execute in delete animal_experiment ")
                cnx.commit()
                return "Success", 201
            except AttributeError:
                raise errors.OperationalError("MySQL Connection not available.")
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return None
            finally:
                cursor.close()
                cnx.close()

class TableHealthAdd(Resource):
    def get(self, animalname):
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("""SELECT Animal_ID FROM animal_table WHERE animalname = %s""", (animalname,))
            rows = cursor.fetchall()
            print("Fetch Completed")
            print(rows)
            cursor.close()
            cnx.close()
            return jsonify(rows)

    def post(self):
        data=request.get_json(force=True)
        print(data)
        for k, v in data.iteritems():
            print >> sys.stderr, ("Code : {0} ==> Value : {1}".format(k, v))
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = cnx.cursor(dictionary=True)
            print("here in health add class from the API call")
            insert_animaldata = ("""INSERT INTO medical_record (result,Animal_id,create_date,medical_notes,location,Amt_given,route,water_feed,
                                    withdraw_time,email_id,Medicine_ID)  VALUES( %(result)s,%(Animal_id)s,%(create_date)s,%(medical_notes)s, 
                                    %(location)s, %(Amt_given)s,%(route)s,%(water_feed)s,%(withdraw_time)s,%(email_id)s,%(Medicine_ID)s )""")
            update_formulary=("""UPDATE formulary SET qty_in_stock=qty_in_stock-%(Amt_given)s where Medicine_ID=%(Medicine_ID)s""")
            try:
                cursor.execute(insert_animaldata, data)
                cursor.execute(update_formulary, data)
                print("here after execute in health add")
                cnx.commit()
                return "Success", 201
            except AttributeError:
                raise errors.OperationalError("MySQL Connection not available.")
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return None
            finally:
                cursor.close()
                cnx.close()

    def patch(self,Animal_id):
        print >> sys.stderr, "Execution started in Repro"
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                return err
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                return err
            else:
                print(err)
                return err
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("""SELECT a.animalname,ID,r.Animal_id, breeding, pregnancy, calfdob,damageatbirth,
                                    siblingcode, calfatside, totalcalves, previouscalf, currentcalf,calfbirthweight,
                                    calfsex, r.email_id, pasturenumber, damcalvingdisposition, calvingease,udderscore,
                                    conditionscorecalving,hiphtweaning,hiphtbreeding,damdisposition,cowframescore,cowwtbreeding,
                                    cowhtbreeding,cowwtweaning,cowhtweaning,cowwtcalving,cowhtcalving,bcsweaning,bcscalving,bcsbreeding,
                                    customcowwt,customcowht,bulldisposition,bullframescore,bullwtprebreeding,bullhtprebreeding,
                                    fertility,mobility,conc,deadabnormal,date from reproduction r,animal_table a where a.Animal_ID=r.Animal_id and r.Animal_id=%s""",Animal_id)
            rows = cursor.fetchall()
            print("Fetch Completed")
            cursor.close()

            cnx.close()

        return jsonify(rows)

class TableReproduction(Resource):
    def get(self):
        print >> sys.stderr, "Execution started in Repro"
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                return err
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                return err
            else:
                print(err)
                return err
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("""SELECT a.animalname,ID,r.Animal_id, breeding, pregnancy, calfdob,damageatbirth,
                                    siblingcode, calfatside, totalcalves, previouscalf, currentcalf,calfbirthweight,
                                    calfsex, r.email_id, pasturenumber, damcalvingdisposition, calvingease,udderscore,
                                    conditionscorecalving,hiphtweaning,hiphtbreeding,damdisposition,cowframescore,cowwtbreeding,
                                    cowhtbreeding,cowwtweaning,cowhtweaning,cowwtcalving,cowhtcalving,bcsweaning,bcscalving,bcsbreeding,
                                    customcowwt,customcowht,bulldisposition,bullframescore,bullwtprebreeding,bullhtprebreeding,
                                    fertility,mobility,conc,deadabnormal,date from reproduction r,animal_table a where a.Animal_ID=r.Animal_id""")
            rows = cursor.fetchall()
            print("Fetch Completed")
            cursor.close()

            cnx.close()

        return jsonify(rows)

    def post(self):
        data=request.get_json(force=True)
        print(data)
        for k, v in data.iteritems():
            print >> sys.stderr, ("Code : {0} ==> Value : {1}".format(k, v))
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = cnx.cursor(dictionary=True)
            print("here in repro class from the API call")
            #insert_animaldata= """INSERT INTO animal_table (animalname,DOB,email_id) VALUES (%(animalname)s,%(calfdob)s,%(email_id)s) """
            insert_animaldata = ("""INSERT INTO animal_table(animalname, animaltype, eartag, eid, pasture_ID, weight,
                                     height, gender, sex, breed, status, current_expt_no, Herd, breeder, currentframescore,
                                     damframescore, comments, species, email_id, brand, brandlocation, tattooleft, tattooright,
                                     alternativeid, registration, color, hornstatus, dam, sire, DOB, howacquired, dateacquired,
                                     howdisposed, datedisposed, disposalreason, herdnumberlocation, herdstatus,
                                     howconceived, managementcode, ownerID, springfall, includeinlookups)
                                     VALUES( %(animalname)s, '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',%(email_id)s, '0', '0', '0',
                                     '0', '0', '0', '0', '0', '0', '0',%(calfdob)s, '0', '1960-01-01', '0','1960-01-01', '0', '0', '0', '0', '0', '0', '0', '0')""")



            try:
                cursor.execute(insert_animaldata, data)
                #cnx.commit()
                print("committed")
                cursor = cnx.cursor(dictionary=True)
                select_animal = """select distinct Animal_ID,animalname,DOB from animal_table where animalname=%(animalname)s"""
                cursor.execute(select_animal, data)
                print("after select stmt")
                rows = cursor.fetchall()
                for row in rows:
                    print("* {Animal_ID}".format(Animal_ID=row['Animal_ID']))
                # for k, v in rows.iteritems():
                #     if k=="Animal_id":
                #         print("inside if")
                #         res=v
                #res=1120
                Animal_ID=rows[0]['Animal_ID']
                print Animal_ID
                data['Animal_ID'] = Animal_ID
                insert_reproductiondata = ("""INSERT INTO reproduction (Animal_id , breeding, pregnancy, calfdob,damageatbirth,
                                                    siblingcode, calfatside, totalcalves, previouscalf, currentcalf,calfbirthweight,
                                                    calfsex, damcalvingdisposition, calvingease,udderscore, email_id,
                                                    conditionscorecalving,hiphtweaning,hiphtbreeding,damdisposition,cowframescore,cowwtbreeding,
                                                    cowhtbreeding,cowwtweaning,cowhtweaning,cowwtcalving,cowhtcalving,bcsweaning,bcscalving,bcsbreeding,
                                                    customcowwt,customcowht,bulldisposition,bullframescore,bullwtprebreeding,bullhtprebreeding,
                                                    fertility,mobility,conc,deadabnormal,date)
                                                    VALUES( %(Animal_ID)s,%(breeding)s,%(pregnancy)s, %(calfdob)s,%(damageatbirth)s,%(siblingcode)s,
                                                    %(calfatside)s, %(totalcalves)s,%(previouscalf)s,%(currentcalf)s,%(calfbirthweight)s,%(calfsex)s,%(damcalvingdisposition)s,
                                                    %(calvingease)s, %(udderscore)s,%(email_id)s,%(conditionscorecalving)s,%(hiphtweaning)s,%(hiphtbreeding)s,
                                                    %(damdisposition)s,%(cowframescore)s,%(cowwtbreeding)s,%(cowhtbreeding)s,%(cowwtweaning)s,%(cowhtweaning)s,%(cowwtcalving)s,
                                                    %(cowhtcalving)s,%(bcsweaning)s,%(bcscalving)s,%(bcsbreeding)s,%(customcowwt)s,%(customcowht)s,%(bulldisposition)s,%(bullframescore)s,
                                                    %(bullwtprebreeding)s,%(bullhtprebreeding)s,%(fertility)s,%(mobility)s,%(conc)s,%(deadabnormal)s,%(date)s)""")
                cursor.execute(insert_reproductiondata,data)
                print("here after execute in repro")
                cnx.commit()
                return "Success", 201
            except AttributeError as e:
                print e
                #raise errors.OperationalError("MySQL Connection not available.")
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return None
            finally:
                cursor.close()
                cnx.close()

    def patch(self):
        print("in repro patch")
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            data = request.get_json(force=True)
            print(data)
            for k, v in data.iteritems():
                print >> sys.stderr, ("Code : {0} ==> Value : {1}".format(k, v))
            cursor = cnx.cursor(dictionary=True)
            print("repro update++++")
            update_animaldata = ("""UPDATE reproduction SET pregnancy=%(pregnancy)s,calfdob=%(calfdob)s,conc=%(conc)s,
                                                damageatbirth=%(damageatbirth)s,siblingcode=%(siblingcode)s,calfatside=%(calfatside)s,totalcalves=%(totalcalves)s,
                                                previouscalf=%(previouscalf)s,currentcalf=%(currentcalf)s,calfbirthweight=%(calfbirthweight)s,
                                                calfsex=%(calfsex)s, damcalvingdisposition=%(damcalvingdisposition)s,calvingease=%(calvingease)s,
                                                udderscore=%(udderscore)s, conditionscorecalving =%(conditionscorecalving)s,hiphtweaning=%(hiphtweaning)s,
                                                email_id=%(email_id)s,pasturenumber=%(pasturenumber)s,hiphtbreeding=%(hiphtbreeding)s,damdisposition=%(damdisposition)s,
                                                cowframescore=%(cowframescore)s,cowwtbreeding=%(cowwtbreeding)s,cowhtbreeding=%(cowhtbreeding)s,cowwtweaning=%(cowwtweaning)s,cowhtweaning=%(cowhtweaning)s,
                                                cowwtcalving=%(cowwtcalving)s,cowhtcalving=%(cowhtcalving)s,bcsweaning=%(bcsweaning)s,bcscalving=%(bcscalving)s,bcsbreeding=%(bcsbreeding)s,
                                                customcowwt=%(customcowwt)s,customcowht=%(customcowht)s,bulldisposition=%(bulldisposition)s,bullframescore=%(bullframescore)s,bullwtprebreeding=%(bullwtprebreeding)s,
                                                bullhtprebreeding=%(bullhtprebreeding)s,fertility=%(fertility)s,mobility=%(mobility)s,deadabnormal=%(deadabnormal)s,date=%(date)s
                                                WHERE ID =%(ID)s """)
            try:
                cursor.execute(update_animaldata,data)
                print("here after execute in update repro ")
                cnx.commit()
                return "Success", 201
            finally:
                cursor.close()
                cnx.close()

    def delete(self,ID):
        # data = request.get_json(force=True)
        print("delete method++")
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = cnx.cursor(dictionary=True)
            print("repro delete++++")
            update_animaldata = "DELETE FROM reproduction WHERE ID = %s "
            try:
                cursor.execute(update_animaldata, (ID,))
                print("here after execute in delete repro ")
                cnx.commit()
                return "Success", 201
            except AttributeError:
                raise errors.OperationalError("MySQL Connection not available.")
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return None
            finally:
                cursor.close()
                cnx.close()
class Expt(Resource):
    def get(self):
        print >> sys.stderr, "Execution started"
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                return err
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                return err
            else:
                print(err)
                return err
        else:
            cursor = cnx.cursor(dictionary=True)
            # cursor.execute("select * from herd")
            cursor.execute("""select a.animalname,e.animaltype,e.birthweight,e.birthweightadj,e.sireframescore,e.bcsrecent,e.bcsprevious,e.bcsdifference,
                                    e.damwtatwean,e.weanheight,e.weanweight,e.weandate,e.weangpd,e.weanwda,e.weanweightdate,e.adj205w,e.adj205h,e.weanframescore,e.ageatwean,
                                    e.yearlingweight,e.yearlingheight,e.yearlingdate,e.adjyearlingw,e.adjyearlingh,e.yearlingframescore,e.ageatyearling,e.customweight,
                                    e.customweightdate,e.customheight,e.customheightdate,e.currentwtcow,e.adj365dht,e.currentwtheifer,e.backfat,e.treatment,e.blockpen,
                                    e.replicate,e.email_id,e.Animal_ID,e.expt_date,e.expt_name from animal_table a,experiments e where a.Animal_ID=e.Animal_ID  order by expt_date desc""")
            rows = cursor.fetchall()
            print("Fetch Completed")
            cursor.close()

            cnx.close()

            return jsonify(rows)

class TableInspection(Resource):
    def get(self):
        print >> sys.stderr, "Execution started in inspection"
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                return err
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                return err
            else:
                print(err)
                return err
        else:
            cursor = cnx.cursor(dictionary=True)
            # cursor.execute("select * from herd")
            cursor.execute("""select * from inspection_report""")
            rows = cursor.fetchall()
            print("Fetch Completed")
            cursor.close()

            cnx.close()

            return jsonify(rows)

    def post(self):
        data=request.get_json(force=True)
        print(data)
        for k, v in data.iteritems():
            print >> sys.stderr, ("Code : {0} ==> Value : {1}".format(k, v))
        try:
            cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='new_barn')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = cnx.cursor(dictionary=True)
            print("here in inspection add class from the API call")
            insert_animaldata = ("""INSERT INTO inspection_report (pasture_ID,general_appearance,live_stock,date,animal_condition,fencing,access_to_food,access_to_water,
                                    cleaniness_of_water,email_ID,access_to_shelter,comments,pasture_major_deficiencies,pasture_minor_deficiencies,builinding_number,lighting,housekeeping,
                                    head_catch_condition,non_slip_surface_evidence,Pen_condition,container_disposal,drug_storage) 
                                     VALUES( %(pasture_ID)s,%(general_appearance)s,%(live_stock)s,%(date)s, %(animal_condition)s, %(fencing)s,%(access_to_food)s,%(access_to_water)s,
                                     %(cleaniness_of_water)s,%(email_ID)s,%(access_to_shelter)s,%(comments)s,%(pasture_major_deficiencies)s,%(pasture_minor_deficiencies)s,%(builinding_number)s,%(lighting)s,
                                      %(housekeeping)s,%(head_catch_condition)s,%(non_slip_surface_evidence)s,%(Pen_condition)s,%(container_disposal)s,%(drug_storage)s)""")

            try:
                cursor.execute(insert_animaldata, data)
                print("here after execute in inspection add")
                cnx.commit()
                return "Success", 201
            except AttributeError as e:
                print e
                raise errors.OperationalError("MySQL Connection not available.")
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return None
            finally:
                cursor.close()
                cnx.close()
